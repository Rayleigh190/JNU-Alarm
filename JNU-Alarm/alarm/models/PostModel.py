from django.db import models

class HomePost(models.Model):
  topic = models.TextField()
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
class CollegePost(models.Model):
  topic = models.TextField()
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

class DepartmentPost(models.Model):
  topic = models.TextField()
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title