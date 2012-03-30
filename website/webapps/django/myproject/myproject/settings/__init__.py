# flake8: noqa
"""
Django settings split into different files for better maintenance and
visibility.
"""
from myproject.settings.base_settings import *
from myproject.settings.installed_apps import *
from myproject.settings.staticfiles_settings import *
from myproject.settings.middleware_settings import *
from myproject.settings.django_settings import *
from myproject.settings.templates_settings import *
from myproject.settings.local.local_settings import *
