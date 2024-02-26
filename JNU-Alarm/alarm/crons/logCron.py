import os
from django.conf import settings
from datetime import datetime, timedelta
# BASE_DIR에 접근하여 파일 경로 구성

def change_cron_log_name():
  os.rename(
    os.path.join(settings.BASE_DIR, 'alarm/log/cron_log/today.log'), 
    os.path.join(settings.BASE_DIR, f'alarm/log/cron_log/{datetime.now().strftime("%Y-%m-%d")}.log')
  )

# def change_uwsgi_log_name():
#   yesterday = datetime.now() - timedelta(days=1)
#   os.rename(
#     os.path.join(settings.BASE_DIR, '/var/log/uwsgi/JNU-Alarm/today.log'), 
#     os.path.join(settings.BASE_DIR, f'/var/log/uwsgi/JNU-Alarm/{yesterday.strftime("%Y-%m-%d")}.log')
#   )