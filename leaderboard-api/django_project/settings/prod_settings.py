import os
from .base_settings import *
from .apps_settings import *

# Default message for testing purposes
SETTINGS_MODULE = "prod"
print("Using Production.")

ALLOWED_HOSTS = ['*']
DEBUG = False

""" Production PostgreSQL Database """
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
