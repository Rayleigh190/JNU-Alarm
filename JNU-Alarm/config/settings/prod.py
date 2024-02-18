from .base import *

Debug = False

ALLOWED_HOSTS = [env('AWS_IP')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # engine: mysql
        'NAME' : env('DB_NAME'),
        'USER' : env('DB_USER'),
        'PASSWORD' : env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': '3306',
        'OPTIONS':{
            'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

WSGI_APPLICATION = 'config.wsgi.prod.application'

## CRONTAB
CRONTAB_DJANGO_SETTINGS_MODULE = 'config.settings.prod'