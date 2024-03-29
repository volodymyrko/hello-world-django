from django.db import models
from django.db.models.signals import post_save, post_delete
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.contenttypes import generic
from django.db.utils import DatabaseError

# Create your models here.

IGNORE_MODEL_LIST = getattr(settings, 'IGNORE_MODEL_LIST', ()) + (
    'session', 'httprequestentry', 'logentry', 'modelactionlog', 'contenttype',
    'site', 'migrationhistory', 'permission',
)

ACTIONS = {
    True: 'create',
    False: 'edit',
    None: 'delete'
}


class HttpRequestEntry(models.Model):
    """model for store http request for db
    """
    path = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    remote_addr = models.CharField(max_length=20)
    priority = models.IntegerField(default=0)

    def __unicode__(self):
        time = self.time.strftime("%Y-%m-%d %H:%M:%S")
        return '%s - %s (%s)' % (self.path[:20], self.remote_addr, time)

    class Meta:
        db_table = 'http_request'
        ordering = ['id']


class ModelActionLog(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    model_name = models.CharField(max_length=50)
    object_str = models.CharField(max_length=200, blank=True)
    object_id = models.IntegerField()
    action = models.CharField(max_length=10)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        time = self.time.strftime("%Y-%m-%d %H:%M:%S")
        return '%s - %s (%s)' % (self.model_name,
            self.action, time)

    class Meta:
        db_table = 'modelactionlog'
        ordering = ['-time']


def log_action(sender, instance, **kwargs):

    model_name = ContentType.objects.get_for_model(instance).model
    if model_name not in IGNORE_MODEL_LIST:
        action = ACTIONS[kwargs.get('created')]
        object_str = instance.__str__()[:200]
        try:
            ModelActionLog.objects.create(model_name=model_name,
                object_str=object_str, object_id=instance.id, action=action,
                content_object=instance)
        except DatabaseError:
            pass

post_save.connect(log_action)
post_delete.connect(log_action)
