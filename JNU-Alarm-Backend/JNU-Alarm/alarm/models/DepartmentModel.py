from django.db import models

## 학과
class Department(models.Model):
  software_engineering = models.BooleanField(default=False)  # 소프트웨어공학과
  electric_engineering = models.BooleanField(default=False)  # 전자공학과