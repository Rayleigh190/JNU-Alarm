from django.db import models

## 단과대 알림 설정
class CollegeSet(models.Model):
  cba = models.BooleanField(default=False) # 경영대학
  eng = models.BooleanField(default=False) # 공과대학
  agric = models.BooleanField(default=False) # 농업생명과학대학
  education = models.BooleanField(default=False) # 사범대학
  socsci = models.BooleanField(default=False) # 사회과학대학
  humanecology = models.BooleanField(default=False) # 생활과학대학
  vetmed = models.BooleanField(default=False) # 수의과대학
  pharmacy = models.BooleanField(default=False) # 약학대학
  arts = models.BooleanField(default=False) # 예술대학
  # medicine = models.BooleanField(default=False) # 의과대학 > 페이지 형태 다름
  human = models.BooleanField(default=False) # 인문대학
  natural = models.BooleanField(default=False) # 자연과학대학
  cvg = models.BooleanField(default=False) # AI융합대학
  engc = models.BooleanField(default=False) # 공학대학(여수)
  yculture = models.BooleanField(default=False) # 문화사회과학대학(여수)
  sea = models.BooleanField(default=False) # 수산해양대학(여수)

class CollegePost(models.Model):
  topic = models.TextField()
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title