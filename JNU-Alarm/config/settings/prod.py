from .base import *

Debug = False

ALLOWED_HOSTS = []

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env,
#         'USER': env('USER'),
#         'PASSWORD': env('PASSWORD')
#     }
# }

## CRONTAB
CRONTAB_DJANGO_SETTINGS_MODULE = 'config.settings.prod'