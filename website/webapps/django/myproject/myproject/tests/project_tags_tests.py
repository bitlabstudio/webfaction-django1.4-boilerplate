"""Tests for the templatetags of the ``project-kairos`` project."""
from django.test import RequestFactory, TestCase

from myproject.templatetags.project_tags import navactive


class NavactiveTestCase(TestCase):
    """Tests for the ``navactive`` templatetag."""
    def test_tag(self):
        req = RequestFactory().get('/foo/bar/')
        result = navactive(req, 'foo')
        self.assertEqual(result, 'active', msg=(
            "When the given string is part of the current request's URL path"
            " it should return ``active`` but returned %s" % result))
        result = navactive(req, 'foobar')
        self.assertEqual(result, '', msg=(
            "When the given string is not part of the current request's URL"
            " path it should return '' but returned %s" % result))

        result = navactive(req, '/foo/bar/', exact=True)
        self.assertEqual(result, 'active', msg=(
            "When the given string is equal to the current request's URL path"
            " it should return ``active`` but returned %s" % result))
        result = navactive(req, '/foo/', exact=True)
        self.assertEqual(result, '', msg=(
            "When the given string is not equal to the current request's URL"
            " path it should return '' but returned %s" % result))

        result = navactive(req, '/')
        self.assertEqual(result, '', msg=(
            'When the given string is / (home) and exact=0, it should'
            ' still return "" even though / is part of the url (otherwise'
            ' the home URL would always be active for all urls and sometimes'
            ' using exact=1 is not an option)'))

        req = RequestFactory().get('/')
        result = navactive(req, '/')
        self.assertEqual(result, 'active', msg=(
            'When the given string is / (home) and the current URL is indeed'
            ' / then it should return "active"'))
