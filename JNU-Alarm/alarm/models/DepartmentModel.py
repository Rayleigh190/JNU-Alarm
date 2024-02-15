from django.db import models

## 간호대학
class NursingDepartment(models.Model):
  nursing = models.BooleanField(default=False)  # 간호학과

## 경영대학
class BusinessAdministration(models.Model):
  business_administration = models.BooleanField(default=False)  # 경영학부
  economics = models.BooleanField(default=False)  # 경제학부

## 공과대학
class EngineeringDepartment(models.Model):
  architecture = models.BooleanField(default=False)  # 건축학부
  materials_engineering = models.BooleanField(default=False)  # 고분자융합소재공학부
  mechanical_engineering = models.BooleanField(default=False)  # 기계공학부
  biotechnology = models.BooleanField(default=False)  # 생물공학과
  materials_science_engineering = models.BooleanField(default=False)  # 신소재공학부
  energy_resource_engineering = models.BooleanField(default=False)  # 에너지자원공학과
  chemical_engineering = models.BooleanField(default=False)  # 화학공학부
  electrical_engineering = models.BooleanField(default=False)  # 전기공학과
  electric_engineering = models.BooleanField(default=False)  # 전자공학과
  electronics_computer_engineering = models.BooleanField(default=False)  # 컴퓨터정보통신공학과
  software_engineering = models.BooleanField(default=False)  # 소프트웨어공학과
  civil_engineering = models.BooleanField(default=False)  # 토목공학과
  environmental_energy_engineering = models.BooleanField(default=False)  # 환경에너지공학과

## 농업생명과학대학
class AgricultureLifeSciences(models.Model):
  applied_plant_science= models.BooleanField(default=False)  # 응용식물학과
  horticulture_science= models.BooleanField(default=False)  # 원예생명공학과
  applied_biology= models.BooleanField(default=False)  # 응용생물학과
  forest_resources= models.BooleanField(default=False)  # 산림자원학과
  forestry_Engineering= models.BooleanField(default=False)  # 임산공학과
  agricultural_biological_chemistry= models.BooleanField(default=False)  # 농생명화학과
  food_engineering= models.BooleanField(default=False)  # 식품공학과
  molecular_biotechnology= models.BooleanField(default=False)  # 분자생명공학과
  animal_science= models.BooleanField(default=False)  # 동물자원학부
  rural_bio_systems_engineering= models.BooleanField(default=False)  # 지역·바이오시스템공학과
  agricultural_economics= models.BooleanField(default=False)  # 농업경제학과
  landscape_architecture= models.BooleanField(default=False)  # 조경학과
  bioenergy_science_technology= models.BooleanField(default=False)  # 바이오에너지공학과
  convergence_biosystems_engineering= models.BooleanField(default=False)  # 융합바이오시스템기계공학과

## 사범대학
class Education(models.Model):
  korean_education= models.BooleanField(default=False)  # 국어교육과
  english_education= models.BooleanField(default=False)  # 영어교육과
  education= models.BooleanField(default=False)  # 교육학과
  early_childhood_education= models.BooleanField(default=False)  # 유아교육과
  geography_education= models.BooleanField(default=False)  # 지리교육과
  history_education= models.BooleanField(default=False)  # 역사교육과
  ethics_education= models.BooleanField(default=False)  # 윤리교육과
  mathematics_education= models.BooleanField(default=False)  # 수학교육과
  physics_education= models.BooleanField(default=False)  # 물리교육과
  chemistry_education= models.BooleanField(default=False)  # 화학교육과
  biology_education= models.BooleanField(default=False)  # 생물교육과
  earth_science_education= models.BooleanField(default=False)  # 지구과학교육과
  home_economics_education= models.BooleanField(default=False)  # 가정교육과
  music_education= models.BooleanField(default=False)  # 음악교육과
  physical_education= models.BooleanField(default=False)  # 체육교육과
  special_education= models.BooleanField(default=False)  # 특수교육학부

## 사회과학대학
# class SocialSciences(models.Model):
#   = models.BooleanField(default=False)  # 정치외교학과
#   = models.BooleanField(default=False)  # 사회학과
#   = models.BooleanField(default=False)  # 심리학과
#   = models.BooleanField(default=False)  # 문헌정보학과
#   = models.BooleanField(default=False)  # 신문방송학과
#   = models.BooleanField(default=False)  # 지리학과
#   = models.BooleanField(default=False)  # 문화인류고고학과
#   = models.BooleanField(default=False)  # 행정학과


## 학과
class Department(models.Model):
  nursing_department = models.ForeignKey(NursingDepartment, on_delete=models.CASCADE)
  business_administration = models.ForeignKey(BusinessAdministration, on_delete=models.CASCADE)
  engineering_department = models.ForeignKey(EngineeringDepartment, on_delete=models.CASCADE)
  agriculture_life_sciences = models.ForeignKey(AgricultureLifeSciences, on_delete=models.CASCADE)
  education = models.ForeignKey(Education, on_delete=models.CASCADE)

## 건축학부
class Architecture(models.Model):
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

## 고분자융합소재공학부
class MaterialsEngineering(models.Model):
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

## 기계공학부
class MechanicalEngineering(models.Model):
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

## 생물공학과
class Biotechnology(models.Model):
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
## 신소재공학부
class MaterialsScienceEngineering(models.Model):
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

## 소프트웨어공학과
class SoftwareEngineering(models.Model):
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title