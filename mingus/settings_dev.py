# -*- coding: utf-8 -*-
import warnings

from mingus.settings import *

LOCAL_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# sorl-thumbnail
THUMBNAIL_DEBUG = True

# django-contact-form
DEFAULT_FROM_EMAIL = 'contactform@foo'

MANAGERS = (('fooper', 'fooper@example.com'), )

DATABASES = {
    'default': {
        'ENGINE':'sqlite3',
        'NAME': 'dev.db',
        'USER':'',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ABC'
EMAIL_HOST_PASSWORD = 'ABC'
EMAIL_USE_TLS = True

CACHE_BACKEND = 'locmem:///'
CACHE_MIDDLEWARE_SECONDS = 60 * 5

# NOTE: Your IP must be in this file to use django-debug-toolbar:
INTERNAL_IPS = ('127.0.0.1', )

try:
    import debug_toolbar
    INSTALLED_APPS += ('debug_toolbar', )

    # django-debug-toolbar
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
except ImportError:
    warnings.warn("django-debug-toolbar is not installed")

# django-bitly
BITLY_LOGIN = 'USERNAME'
BITLY_API_KEY = 'APIKEYHERE'
