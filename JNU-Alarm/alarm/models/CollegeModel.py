from django.db import models

## 단과대
class CollegeSet(models.Model):
  engineering = models.BooleanField(default=False)  # 공과대
  natural_science = models.BooleanField(default=False)  # 자연과학대

## 공과대학
# class Engineering(models.Model):
#   num = models.PositiveIntegerField()
#   title = models.TextField()
#   created_at = models.DateTimeField(auto_now_add=True)

#   def __str__(self):
#     return self.title