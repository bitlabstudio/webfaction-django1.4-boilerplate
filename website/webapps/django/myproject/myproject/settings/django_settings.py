"""Django related settings."""
import os

from django.contrib import messages

from myproject.settings.base_settings import PROJECT_ROOT


# =================
# General settings
# =================
SITE_ID = 1
ROOT_URLCONF = 'myproject.urls'

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-error',
}

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'myproject/fixtures'),
)


# =======================
# Email related settings
# =======================
SEND_BROKEN_LINK_EMAILS = True


# =============================
# Language & Timezone settings
# =============================
gettext = lambda s: s

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'
USE_TZ = True

# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
LANGUAGES = (
    ('en', gettext('English')),
)
