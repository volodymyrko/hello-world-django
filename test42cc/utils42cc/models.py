from django.db import models

# Create your models here.


class HttpRequestEntry(models.Model):
    """model for store http request for db
    """
    path = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    remote_addr = models.CharField(max_length=20)

    def __unicode__(self):
        time = self.time.strftime("%Y-%m-%d %H:%M:%S")
        return '%s - %s (%s)' % (self.path[:20], self.remote_addr, time)

    class Meta:
        db_table = 'http_request'
        ordering = ['id']
