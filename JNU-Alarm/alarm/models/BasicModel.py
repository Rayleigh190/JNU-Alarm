from django.db import models

## 기본
class BasicSet(models.Model):
  weather = models.BooleanField(default=False)  # 날씨
  emergency = models.BooleanField(default=False)  # 긴급