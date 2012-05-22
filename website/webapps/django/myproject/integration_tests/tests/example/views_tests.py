"""Integration tests for the ``APPNAME`` app."""
from django.core.urlresolvers import reverse
from django.test import TestCase


class ViewNameTestCase(TestCase):
    """Tests for the ``ViewName`` view class."""
    def get_view_name(self):
        return 'view_name'

    def test_view_is_callable(self):
        resp = self.client.get(reverse(self.get_view_name()))
        self.assertEqual(resp.status_code, 200)
