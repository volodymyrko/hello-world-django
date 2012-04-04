"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import unittest
from django.test.client import Client
from contact.models import Contact

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ContactTest(unittest.TestCase):
    def setUp(self):
        Contact.objects.create(name='test_name', surname='test_surname',
            birthday='01.01.1970', email='test@testing.local', jabber='jabber@test',
            skype='test_skype', contacts='test_contacts')

    def test_contact_creation(self):
        """ test for Contact objects creation
        """
        self.assertTrue(Contact.objects.count() > 0)
        test_contact = Contact.objects.get(name='test_name')
        self.assertEqual(test_contact.surname, 'test_surname')
    
    def test_index_page(self):
        """ test http code for index page 
        """
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
