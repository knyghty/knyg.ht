from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Page


class PageTests(TestCase):
    def test_404(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_home(self):
        Page.objects.create(
            url='',
            title='Home',
            icon='fa fa-home',
            content='<p>Test</p>',
            position=10
        )

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<p>Test</p>')

    def test_subpage(self):
        root = Page.objects.create(
            url='',
            title='Home',
            icon='fa fa-home',
            content='<p>Test</p>',
            position=10
        )

        Page.objects.create(
            url='test',
            title='Test',
            icon='fa fa-test',
            content='<p>Subpage</p>',
            position=10,
            parent=root
        )

        response = self.client.get(reverse('page', args=('test',)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<p>Subpage</p>')
