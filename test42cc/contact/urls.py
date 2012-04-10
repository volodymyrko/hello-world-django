""" url schema for app contact
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('contact.views',
    url('^$', 'index', name='index'),
    url('^edit/$', 'edit', name='edit'),
    )
