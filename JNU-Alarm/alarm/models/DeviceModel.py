from django.db import models
from .SettingModel import Setting


class Device(models.Model):
  device_id = models.TextField(unique=True, blank=False, null=False)
  setting = models.ForeignKey(Setting, on_delete=models.CASCADE)

  def __str__(self):
      return self.device_id

class Notification(models.Model):
  device = models.ForeignKey(Device, on_delete=models.CASCADE)
  title = models.TextField()
  body = models.TextField()
  link = models.URLField()
  created_at = models.DateTimeField(auto_now_add=True)