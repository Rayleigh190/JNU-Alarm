from django.db import models


class Department(models.Model):
  software_engineering = models.BooleanField(default=False)
  electric_engineering = models.BooleanField(default=False)

class College(models.Model):
  engineering = models.BooleanField(default=False)
  natural_science = models.BooleanField(default=False)

class Setting(models.Model):
  college = models.ForeignKey(College, on_delete=models.CASCADE)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)

class User(models.Model):
  device_id = models.TextField(unique=True)
  fcm_token = models.TextField(unique=True)
  setting = models.ForeignKey(Setting, on_delete=models.CASCADE)