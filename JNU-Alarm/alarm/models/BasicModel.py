from django.db import models

class Notification(models.Model):
  topic = models.TextField()
  title = models.TextField()
  body = models.TextField()
  link = models.URLField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title


class Question(models.Model):
  email = models.EmailField()
  title = models.TextField()
  content = models.TextField()
  is_completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  

class Device(models.Model):
  device_id = models.TextField()
  subscribed_topics = models.JSONField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  is_agree = models.BooleanField(default=True)
  is_test_device = models.BooleanField(default=False)
  memo = models.TextField(blank=True)
  is_iOS = models.BooleanField(default=True)