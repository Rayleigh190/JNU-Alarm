from django.db import models
from .BasicModel import Basic
from .CollegeModel import College
from .DepartmentModel import Department

## 전체 설정
class Setting(models.Model):
  basic = models.ForeignKey(Basic, on_delete=models.CASCADE)  # 기본
  college = models.ForeignKey(College, on_delete=models.CASCADE)  # 단과대
  department = models.ForeignKey(Department, on_delete=models.CASCADE)  # 학과