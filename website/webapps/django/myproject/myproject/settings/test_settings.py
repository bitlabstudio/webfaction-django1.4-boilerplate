# flake8: noqa
"""Settings to be used for running tests."""
from myproject.settings import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

EMAIL_SUBJECT_PREFIX = '[test] '
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
SOUTH_TESTS_MIGRATE = False
