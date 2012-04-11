from django.db import models
import Image

# Create your models here.

PHOTO_WIDTH = 200
PHOTO_HEIGHT = 300


class Contact(models.Model):
    """ present my Contact in db
    """
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=50, blank=True)
    contacts = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo', blank=True)

    def __unicode__(self):
        return self.name + ' ' + self.surname

    class Meta:
        db_table = 'contact'
        ordering = ['id']

    def save(self, *args, **kwargs):
        """ resize image if large
        """
        super(Contact, self).save(*args, **kwargs)
        if self.photo:
            image = Image.open(self.photo.path)
            if image.mode not in ('L', 'RGB'):
                image = image.convert('RGB')
            width = image.size[0]
            height = image.size[1]
            if width > PHOTO_WIDTH or height < PHOTO_HEIGHT:
                w_ratio = width / float(PHOTO_WIDTH)
                h_ratio = height / float(PHOTO_HEIGHT)
                ratio = w_ratio if w_ratio > h_ratio else h_ratio
                dest_width = int(width / ratio)
                dest_height = int(height / ratio)
                image = image.resize((dest_width, dest_height),
                    Image.ANTIALIAS)
                image.save(self.photo.path)
