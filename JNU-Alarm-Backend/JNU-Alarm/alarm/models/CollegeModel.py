from django.db import models

## 단과대
class College(models.Model):
  engineering = models.BooleanField(default=False)  # 공과대
  natural_science = models.BooleanField(default=False)  # 자연과학대