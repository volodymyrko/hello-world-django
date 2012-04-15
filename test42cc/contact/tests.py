"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from django.utils import unittest
from django.test.client import Client
from contact.models import Contact
from django.core.urlresolvers import reverse

ADMIN_LOGIN = 'admin'
ADMIN_PASSWD = 'admin'


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
        self.test_email = 'me@test.ua'
        self.post_data = {'name': 'Volodya',
            'surname': 'Kovtun', 'email': self.test_email,
            'jabber': 'j@jabber.ua', 'skype': 'skype',
            'contacts': 'contacts', 'bio': 'bio',
            'birthday': '28.07.2012'}

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

    def test_edit(self):
        """ testing /edit/ page
        """
        self.client.login(username=ADMIN_LOGIN, password=ADMIN_PASSWD)
        self.client.post('/edit/', self.post_data)
        page = self.client.get('/')
        self.assertIn(self.test_email, page.content)
        contact = Contact.objects.all()[:1].get()
        self.assertEqual(self.test_email, contact.email)

    def test_edit_ajax(self):
        """ edit with jqeury
        """
        self.client.login(username=ADMIN_LOGIN, password=ADMIN_PASSWD)
        self.client.post('/edit/', self.post_data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        page = self.client.get('/')
        self.assertIn(self.test_email, page.content)
        contact = Contact.objects.all()[:1].get()
        self.assertEqual(self.test_email, contact.email)


class ReverseFromTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.edit = reverse('edit')

    def test_reverse(self):
        """ check field sequence
        """
        self.client.login(username=ADMIN_LOGIN, password=ADMIN_PASSWD)
        page = self.client.get(self.edit).content
        t = '<label for="id_%s">'
        self.assertTrue(page.find(t % 'bio') < page.find(t % 'email') <
            page.find(t % 'surname') < page.find(t % 'name'))
