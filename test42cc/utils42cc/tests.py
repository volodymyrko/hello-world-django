"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from django.utils import unittest
from django.test.client import Client
from django.template import RequestContext
from django.http import HttpRequest
from django.conf import settings
from django.core.urlresolvers import reverse
from utils42cc.models import HttpRequestEntry


class MiddlewareTest(unittest.TestCase):
    def setUp(self):
        """ prepare to testing
        """
        self.client = Client()
        self.url = '/requests'

    def test_middleware(self):
        """ middleware testing for saving urls
        """
        self.client.get(self.url)
        self.assertTrue(HttpRequestEntry.objects.filter(path=self.url))


class ShowRequestsTest(unittest.TestCase):
    def setUp(self):
        """ prepare to testing
        """
        self.client = Client()
        self.url = reverse('requests')

    def test_page_requests(self):
        """ test page for showing visited urls
        """
        page = self.client.get(self.url)
        self.assertIn(self.url, page.content)

    def test_requests(self):
        """ test requests with middleware
        """
        for entry in HttpRequestEntry.objects.all():
            entry.delete()  # clear http request log table

        num = 15
        request_per_page = 10
        t_url = '/request_%s/'
        t_record = '<td>/request_%s/</td>'

        for i in range(num):
            url = t_url % i
            self.client.get(url)

        page = self.client.get(self.url)
        for i in range(num):
            record = t_record % i
            if i < request_per_page:
                self.assertIn(record, page.content)
            else:
                self.assertNotIn(record, page.content)


class ContextProcTest(unittest.TestCase):
    def setUp(self):
        self.context = RequestContext(HttpRequest())
        self.key = 'django_settings'
        self.processors = settings.TEMPLATE_CONTEXT_PROCESSORS
        self.proc = 'utils42cc.context_processors.django_settings'

    def test_context_exists(self):
        self.assertTrue(self.key in self.context)
        self.assertIn(self.proc, self.processors)
