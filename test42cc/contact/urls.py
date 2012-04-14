""" url schema for app contact
"""

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.views import login

urlpatterns = patterns('contact.views',
    url('^$', 'index', name='index'),
    url('^edit/$', 'edit', name='edit'),
    url('^accounts/login/$', login, {'template_name': 'login.html'}),
    )
