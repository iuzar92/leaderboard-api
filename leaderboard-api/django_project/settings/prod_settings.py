import os
from .base_settings import *
from .apps_settings import *

# Default message for testing purposes
SETTINGS_MODULE = "prod"
print("Using Production.")

ALLOWED_HOSTS = ['*']
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1=x5=#g_p&&su9#6yszcyl&z7#^#@64v^)rv(rdgz*o+%1!jv1'

# Production Proxy Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'production',
        'USER': 'dbproduser',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}