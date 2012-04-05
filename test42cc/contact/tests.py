"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from django.utils import unittest
from django.test.client import Client
from contact.models import Contact


class ContactTest(unittest.TestCase):
    def test_contact_creation(self):
        """ test for Contact objects creation
        """
        Contact.objects.create(name='name', surname='surname',
            birthday='01.01.1970', email='t@test.local', jabber='jabber@test',
            skype='skype', contacts='contacts')
        test_contact = Contact.objects.get(name='name')
        self.assertEqual(test_contact.surname, 'surname')
        self.assertTrue(Contact.objects.count() > 0)


class ViewsTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        """ test http code for index page
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_fixture_contact(self):
        """test for data exists loaded with fixtures
        """
        search = 'Volodya'
        response = self.client.get('/')
        self.assertIn(search, response.content)
