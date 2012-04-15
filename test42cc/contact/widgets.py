from django.forms.widgets import TextInput
from django.conf import settings


class CalendarWidget(TextInput):
    class Media:
        css = {
            'all': (settings.STATIC_URL +
                'css/ui-lightness/jquery-ui-1.8.18.custom.css',),
        }
        js = (settings.STATIC_URL + 'js/jquery-1.7.1.min.js',
            settings.STATIC_URL + 'js/jquery-ui-1.8.18.custom.min.js',
            settings.STATIC_URL + 'js/calendarwidget.js',
        )
