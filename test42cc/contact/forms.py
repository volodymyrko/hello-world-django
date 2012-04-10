from django.forms import ModelForm
from contact.models import Contact


class ContactForm(ModelForm):
    """ Form for Contact model
    """
    class Meta:
        model = Contact
        fields = ('name', 'surname', 'birthday',
            'photo', 'email', 'jabber', 'skype',
            'contacts', 'bio')
