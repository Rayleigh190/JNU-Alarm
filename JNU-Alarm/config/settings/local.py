from .base import *

Debug = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

WSGI_APPLICATION = 'config.wsgi.local.application'

## CRONTAB
CRONTAB_DJANGO_SETTINGS_MODULE = 'config.settings.local'