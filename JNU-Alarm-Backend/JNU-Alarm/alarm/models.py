from django.db import models


class Department(models.Model):
  software_engineering = models.BooleanField(default=False)

class Setting(models.Model):
  department = models.ForeignKey(Department, on_delete=models.CASCADE)

class User(models.Model):
  device_id = models.TextField(unique=True)
  fcm_token = models.TextField(unique=True)
  setting = models.ForeignKey(Setting, on_delete=models.CASCADE)