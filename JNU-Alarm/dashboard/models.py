from django.db import models

class Shortcut(models.Model):
  name = models.CharField(max_length=10)
  ios_image_name = models.CharField(max_length=20)
  aos_image_name = models.CharField(max_length=20)
  link = models.URLField()
  is_webview = models.BooleanField()
  is_modal = models.BooleanField()

  def __str__(self):
    return self.name
