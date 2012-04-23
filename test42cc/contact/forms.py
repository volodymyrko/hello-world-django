from django.forms import ModelForm
from django.conf import settings
from django.forms.widgets import Textarea, ClearableFileInput
from django.utils.safestring import mark_safe
from contact.models import Contact
from contact.widgets import CalendarWidget


class PhotoWidget(ClearableFileInput):
    """ widget that show image (<img> tag) with form
    """
    def render(self, name, value, attrs=None):
        result = super(PhotoWidget, self).render(name, value, attrs)
        if value and hasattr(value, 'url'):
            result = mark_safe(u'%s <br /><img src="%s%s" >' % (result,
                settings.STATIC_URL, value.url))
        else:
            result = mark_safe(u'%s<br /><img src="%s%s" >' % (result,
                settings.STATIC_URL, 'img/nophoto.gif'))
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
            'bio': Textarea(attrs={'class': 'block'}),
            'contacts': Textarea(attrs={'class': 'block'}),
            'photo': PhotoWidget(),
            'birthday': CalendarWidget(),
        }
