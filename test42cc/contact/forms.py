from django.forms import ModelForm
from django.conf import settings
from django.forms.widgets import Textarea, ClearableFileInput
from django.utils.safestring import mark_safe
from contact.models import Contact


class BrTextarea(Textarea):
    """ widget that show label_tag and field value in different rows
    """
    def render(self, name, value, attrs=None):
        result = super(BrTextarea, self).render(name, value, attrs=None)
        return mark_safe(u'<br />%s' % result)


class PhotoWidget(ClearableFileInput):
    """ widget that show image (<img> tag) with form
    """
    def render(self, name, value, attrs=None):
        result = super(PhotoWidget, self).render(name, value, attrs=None)
        if value and hasattr(value, 'url'):
            result = mark_safe(u'%s<br /><img src="%s/%s">' % (result,
                settings.STATIC_URL, value.url))
        return result


class ContactForm(ModelForm):
    """ Form for Contact model
    """
    class Meta:
        model = Contact
        fields = ('name', 'surname', 'birthday',
            'photo', 'email', 'jabber', 'skype',
            'contacts', 'bio')
        widgets = {
            'bio': BrTextarea(),
            'contacts': BrTextarea(),
            'photo': PhotoWidget(),
        }
