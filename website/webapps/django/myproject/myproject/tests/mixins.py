"""
Generally useful mixins for tests of any project.

This should be open sourced in the future, so it must be project agnostic.

"""
from django.core.urlresolvers import reverse

from myproject.tests.factories import UserFactory


class ViewTestsMixin(object):
    """Mixin that provides commonly tested assertions."""

    def get_view_name(self):
        """
        Returns the URL of this view by using ``reverse``.

        You must implement this when inheriting this mixin.

        """
        return NotImplementedError

    def get_view_args(self):
        """
        Returns the view's args, if necessary.

        If the URL of this view is constructed via args, you can override this
        method and return the proper args for the test.

        """
        return None

    def get_view_kwargs(self):
        """
        Returns the view's kwargs, if necessary.

        If the URL of this view is constructed via kwargs, you can override
        this method and return the proper args for the test.

        """
        return None

    def get_url(self, view_name=None, view_args=None, view_kwargs=None):
        """
        Returns the request params for this view.

        When calling ``self.client.get`` we usually need three parameter:

            * The URL, which we construct from the view name using ``reverse``
            * The args
            * The kwargs

        In most cases ``args`` and ``kwargs`` are ``None``, so this method will
        help to return the proper URL by calling instance methods that can
        be overridden where necessary.

        """
        if view_name is None:
            view_name = self.get_view_name()
        if view_args is None:
            view_args = self.get_view_args()
        if view_kwargs is None:
            view_kwargs = self.get_view_kwargs()
        return reverse(view_name, args=view_args, kwargs=view_kwargs)

    def login(self, user):
        """Performs a login for the given user."""
        self.client.login(username=user.username, password='test123')

    def should_redirect_to_login_when_anonymous(
            self, view_name=None, view_args=None, view_kwargs=None):
        """Tests if the view redirects to login when the user is anonymous."""
        url = self.get_url(view_name, view_args, view_kwargs)
        resp = self.client.get(url)
        self.assertRedirects(resp,
            '{0}?next={1}'.format(reverse('auth_login'), url))
        return resp

    def should_be_callable_when_anonymous(
            self, view_name=None, view_args=None, view_kwargs=None):
        """Tests if the view returns 200 when the user is anonymous."""
        url = self.get_url(view_name, view_args, view_kwargs)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        return resp

    def should_be_callable_when_authenticated(
            self, user, view_name=None, view_args=None, view_kwargs=None):
        """Tests if the view returns 200 when the user is logged in."""
        url = self.get_url(view_name, view_args, view_kwargs)
        self.login(user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        return resp

    def should_be_callable_when_has_correct_permissions(
            self, user, view_name=None, view_args=None, view_kwargs=None):
        """Tests if the view returns 200 when the user has permissions."""
        url = self.get_url(view_name, view_args, view_kwargs)
        user_no_permissions = UserFactory()
        self.login(user_no_permissions)
        resp = self.client.get(url)
        self.assertRedirects(resp,
            '{0}?next={1}'.format(reverse('auth_login'), url))

        self.login(user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
