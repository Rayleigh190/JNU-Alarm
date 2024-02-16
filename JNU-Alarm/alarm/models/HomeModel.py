from django.db import models

## 홈페이지 알림 설정
class HomeSet(models.Model):
  academic = models.BooleanField(default=False) # 학사안내
  scholarship = models.BooleanField(default=False) # 장학안내

class HomePost(models.Model):
  topic = models.TextField()
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title