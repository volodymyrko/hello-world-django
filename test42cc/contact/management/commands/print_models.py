from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in ContentType.objects.all():
            count = obj.get_all_objects_for_this_type().count()
            self.stdout.write("%s: %s\n" % (obj.model, count))
            self.stderr.write("error: %s: %s\n" % (obj.model, count))
