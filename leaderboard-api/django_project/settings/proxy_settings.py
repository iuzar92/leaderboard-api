import os
from .base_settings import *
from .apps_settings import *

# Default message for testing purposes
SETTINGS_MODULE = "prox"
print("Using Proxy.")

""" Proxy PostgreSQL Database """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'development',
        'USER': 'dbdevuser',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}