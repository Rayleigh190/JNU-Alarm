from .base import *

Debug = False

ALLOWED_HOSTS = [env('AWS_IP')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

WSGI_APPLICATION = 'config.wsgi.prod.application'

## CRONTAB
CRONTAB_DJANGO_SETTINGS_MODULE = 'config.settings.prod'

# CRONJOBS += [
#   ('* 0 * * *', 'alarm.crons.change_uwsgi_log_name', f'>> ' + os.path.join(BASE_DIR, 'alarm/log/cron_log/today.log') + ' 2>&1 '), # 매일 0시
# ]