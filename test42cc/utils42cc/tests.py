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
from django.core.management import call_command
import StringIO
from utils42cc.models import HttpRequestEntry, ModelActionLog

ADMIN_LOGIN = 'admin'
ADMIN_PASSWD = 'admin'


class MiddlewareTest(unittest.TestCase):
    def setUp(self):
        """ prepare to testing
        """
        self.client = Client()
        self.url = '/requests/'

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


class TagTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.index = reverse('index')
        self.search = '/admin/auth/user/1/'

    def test_tag(self):
        self.client.login(username=ADMIN_LOGIN, password=ADMIN_PASSWD)
        page = self.client.get(self.index)
        self.assertIn(self.search, page.content)


class PrintModelsTest(unittest.TestCase):
    def setUp(self):
        self.stdout = StringIO.StringIO()
        self.stderr = StringIO.StringIO()

    def test_command(self):
        """ test print_models command output, test error dupliction
        """
        call_command('print_models', **{'stdout': self.stdout,
            'stderr': self.stderr})
        self.stdout.seek(0)
        self.stderr.seek(0)
        errors = self.stderr.read()

        self.assertTrue(self.stdout.len > 0)
        self.assertTrue(self.stderr.len > 0)

        for line in self.stdout.readlines():
            self.assertIn(u'error: %s' % line, errors)


class ModelActionLogTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.edit = reverse('edit')
        self.post_data = {'name': 'Volodya',
            'surname': 'Kovtun', 'email': 'me@in.ua',
            'jabber': 'j@jabber.ua', 'skype': 'skype',
            'contacts': 'contacts', 'bio': 'bio',
            'birthday': '28.07.2012'}

    def test_store_log(self):
        """ test for store action log with models
        """
        self.client.login(username=ADMIN_LOGIN, password=ADMIN_PASSWD)
        ModelActionLog.objects.all().delete()
        self.client.post(self.edit, self.post_data)
        log = ModelActionLog.objects.all()[:1].get()
        self.assertTrue(ModelActionLog.objects.count() > 0)
        self.assertEqual(log.model_name, 'contact')

    def test_exclude_log(self):
        """ test for exclude operation with some models
        """
        ModelActionLog.objects.all().delete()
        HttpRequestEntry.objects.create(path='test',
            method='TEST', remote_addr='127.0.0.1')
        self.assertTrue(ModelActionLog.objects.count() == 0)


class RequestsPriorityTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.prio = reverse('prio')
        self.page = reverse('requests')

    def test_sequence_order(self):
        HttpRequestEntry.objects.all().delete()
        num = 15
        t_url = '/request_%s/'
        t = '<td>/request_%s/</td>'

        self.client.login(username=ADMIN_LOGIN, password=ADMIN_PASSWD)

        for i in range(num):
            url = t_url % i
            self.client.get(url)

        """ test requests without change priority
        """
        page = self.client.get(self.page).content
        self.assertTrue(page.find(t % '0') < page.find(t % '1') <
            page.find(t % '4') < page.find(t % '7'))

        """ test requests with priority change
        """
        self.client.get(self.prio, {'id': 5, 'action': 'plus'})
        self.client.get(self.prio, {'id': 5, 'action': 'plus'})
        self.client.get(self.prio, {'id': 2, 'action': 'plus'})

        page = self.client.get(self.page).content
        t = '<td>/request_%s/</td>'
        self.assertFalse(page.find(t % '0') < page.find(t % '1') <
            page.find(t % '4') < page.find(t % '7'))
        self.assertTrue(page.find(t % '4') < page.find(t % '1') <
            page.find(t % '0') < page.find(t % '7'))
