import os
from django.conf import settings
from datetime import datetime 
# BASE_DIR에 접근하여 파일 경로 구성

def change_cron_log_name():
  os.rename(
    os.path.join(settings.BASE_DIR, 'alarm/log/cron_log/today.log'), 
    os.path.join(settings.BASE_DIR, f'alarm/log/cron_log/{datetime.now().strftime("%Y-%m-%d")}.log')
  )