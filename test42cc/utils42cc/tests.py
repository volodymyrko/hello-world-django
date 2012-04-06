"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from django.utils import unittest
from django.test.client import Client
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
        self.url = '/requests/'

    def test_page_requests(self):
        """ test page for showing visited urls
        """
        page = self.client.get(self.url)
        self.assertIn(self.url, page.content)
