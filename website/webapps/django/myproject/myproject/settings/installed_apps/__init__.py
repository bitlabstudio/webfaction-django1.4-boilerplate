"""
Apps settings

This file contains the settings.INSTALLED_APPS setting, and imports all
app-related settings, one file per app.
"""
INTERNAL_APPS = [
    'myproject',
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

    # cms apps
    'cms',
    'cms.plugins.text',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'cms.plugins.inherit',
    'mptt',
    'menus',
    'sekizai',

    # filer apps
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    # cmsplugin_blog dependencies
    'cmsplugin_blog',
    'djangocms_utils',
    'simple_translation',
    'tagging',
    'missing',

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
from cms import *  # NOQA
from cmsplugin_blog import *  # NOQA
from contact_form import *  # NOQA
from registration_email import *  # NOQA
