# flake8: noqa
"""
Apps settings

This file contains the settings.INSTALLED_APPS setting, and imports all
app-related settings, one file per app.
"""
import os
import sys


INTERNAL_APPS = [
    '_global',
]

EXTERNAL_APPS = [
    'contact_form',
    'brutebuster_signals',
    'honeypot_signals',

    'south',
    'easy_thumbnails',
    'captcha',
    'admin_honeypot',
    'BruteBuster',

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
from captcha import *
from contact_form import *
from registration_email import *
