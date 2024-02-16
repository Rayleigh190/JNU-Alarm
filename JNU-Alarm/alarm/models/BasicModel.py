from django.db import models

class Notification(models.Model):
  topic = models.TextField()
  title = models.TextField()
  body = models.TextField()
  link = models.URLField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title