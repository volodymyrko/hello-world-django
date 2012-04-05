""" url schema for app contact
"""

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('contact.views',
    url('^$', 'index', name='index'),
    )
