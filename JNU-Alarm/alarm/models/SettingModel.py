from django.db import models
from .BasicModel import BasicSet
from .CollegeModel import CollegeSet
from .DepartmentModel import DepartmentSet

## 전체 설정
class Setting(models.Model):
  basic = models.ForeignKey(BasicSet, on_delete=models.CASCADE)  # 기본
  college = models.ForeignKey(CollegeSet, on_delete=models.CASCADE)  # 단과대
  department = models.ForeignKey(DepartmentSet, on_delete=models.CASCADE)  # 학과