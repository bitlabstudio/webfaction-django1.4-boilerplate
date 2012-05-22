"""
Utilities and helper functions for all tests of ``selfquantified.com``.

The tools in this module shall help to create test fixtures for models that are
global to the project and could be shared by tests of specialized apps.

For example each app will need to create a user, therefore this module shall
provide facilities for user generation.
"""
import datetime
import md5

from django.contrib.auth.models import User

import factory


class UserFactory(factory.Factory):
    """
    Creates a new ``User`` object.

    Username will be a random 30 character md5 value.
    Email will be ``userN@example.com`` with ``N`` being a counter.
    Password will be ``test123`` by default.

    """
    FACTORY_FOR = User

    username = factory.LazyAttribute(
        lambda x: md5.new(datetime.datetime.now().strftime(
            '%Y%,%d%H%M%S')).hexdigest()[0:30])
    email = factory.Sequence(lambda n: 'user{0}@example.com'.format(n))

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = 'test123'
        if 'password' in kwargs:
            password = kwargs.pop('password')
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        user.set_password(password)
        if create:
            user.save()
        return user
