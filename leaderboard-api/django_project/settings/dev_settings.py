import os
from .base_settings import *
from .apps_settings import INSTALLED_APPS

# Default message for testing purposes
SETTINGS_MODULE = "dev"
print("Using Development.")

""" Development PostgreSQL Database """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dev-db',
        'USER': 'dbdevuser',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}