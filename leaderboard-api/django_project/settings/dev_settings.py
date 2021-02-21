import os
from .base_settings import *
from .apps_settings import INSTALLED_APPS

# Default message for testing purposes
SETTINGS_MODULE = "dev"
print("Using Development.")

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}