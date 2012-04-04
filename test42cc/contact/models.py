from django.db import models

# Create your models here.

class Contact(models.Model):
    """ present my Contact
    """
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    contacts = models.TextField(blank=True)

    def __unicode__(self):
        return self.name+' '+self.surname

    class Meta:
        db_table = 'contact'
        ordering = ["id"]
