"""
Apps settings

This file contains the settings.INSTALLED_APPS setting, and imports all
app-related settings, one file per app.
"""
INTERNAL_APPS = [
    '_global',
]

EXTERNAL_APPS = [
    'mailer',
    'contact_form',
    'honeypot_signals',

    'south',
    'easy_thumbnails',
    'captcha',
    'admin_honeypot',

    # registration apps
    'registration',
    'registration_email',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
]

TEST_APPS = INTERNAL_APPS
INSTALLED_APPS = DJANGO_APPS + INTERNAL_APPS + EXTERNAL_APPS

# Apps settings
from captcha import *  # NOQA
from contact_form import *  # NOQA
from registration_email import *  # NOQA
