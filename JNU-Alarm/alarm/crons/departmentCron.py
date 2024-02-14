import pprint
from datetime import datetime
from .baseCron import general_crawling, first_crawling, send_topic_message

from ..models import Device, Department, Architecture, MaterialsEngineering, MechanicalEngineering, Biotechnology, MaterialsScienceEngineering, SoftwareEngineering


## 학과
# 건축학부, archi
def architecture_crawling():
  today = str(datetime.now())
  base_url = "https://archi.jnu.ac.kr"
  url = 'https://archi.jnu.ac.kr/archi/8023/subview.do'
  if Architecture.objects.count() == 0:
    first_crawling(base_url=base_url, url=url, department_model=Architecture)
    print(f"{today} : 건축학부 첫 크롤링")
    return
  posts = general_crawling(base_url=base_url, url=url, department_model=Architecture)
  
  if len(posts) > 0:
    for post in reversed(posts):
      Architecture.objects.create(num=post['num'], title=post['title'])
      isTrue_departments = Department.objects.filter(architecture=True)
      isTrue_devices = Device.objects.filter(setting__department__in=isTrue_departments)
      print(f"{today} : 건축학부 알림 발송")
      pprint.pprint(post)
      send_topic_message("건축학부", post['title'], isTrue_devices, post['url'], 'archi')
  else:
    print(f"{today} : 건축학부 새로운 공지 없음")

# 고분자융합소재공학부, pf
def materials_engineering_crawling():
  today = str(datetime.now())
  base_url = "https://pf.jnu.ac.kr"
  url = 'https://pf.jnu.ac.kr/pf/7821/subview.do'
  if MaterialsEngineering.objects.count() == 0:
    print(f"{today} : 고분자융합소재공학부 첫 크롤링")
    first_crawling(base_url=base_url, url=url, department_model=MaterialsEngineering)
    return
  posts = general_crawling(base_url=base_url, url=url, department_model=MaterialsEngineering)
  
  if len(posts) > 0:
    for post in reversed(posts):
      MaterialsEngineering.objects.create(num=post['num'], title=post['title'])
      isTrue_departments = Department.objects.filter(materials_engineering=True)
      isTrue_devices = Device.objects.filter(setting__department__in=isTrue_departments)
      print(f"{today} : 고분자융합소재공학부 알림 발송")
      pprint.pprint(post)
      send_topic_message("고분자융합소재공학부", post['title'], isTrue_devices, post['url'], 'pf')
  else:
    print(f"{today} : 고분자융합소재공학부 새로운 공지 없음")

# 기계공학부, mech
def mechanical_engineering_crawling():
  today = str(datetime.now())
  base_url = "https://mech.jnu.ac.kr"
  url = 'https://mech.jnu.ac.kr/mech/8218/subview.do'
  if MechanicalEngineering.objects.count() == 0:
    print(f"{today} : 기계공학부 첫 크롤링")
    first_crawling(base_url=base_url, url=url, department_model=MechanicalEngineering)
    return
  posts = general_crawling(base_url=base_url, url=url, department_model=MechanicalEngineering)
  
  if len(posts) > 0:
    for post in reversed(posts):
      MechanicalEngineering.objects.create(num=post['num'], title=post['title'])
      isTrue_departments = Department.objects.filter(mechanical_engineering=True)
      isTrue_devices = Device.objects.filter(setting__department__in=isTrue_departments)
      print(f"{today} : 기계공학부 알림 발송")
      pprint.pprint(post)
      send_topic_message("기계공학부", post['title'], isTrue_devices, post['url'], 'mech')
  else:
    print(f"{today} : 기계공학부 새로운 공지 없음")

# 생물공학과, bte
def biotechnology_crawling():
  today = str(datetime.now())
  base_url = "https://bte.jnu.ac.kr"
  url = 'https://bte.jnu.ac.kr/bte/10981/subview.do'
  if Biotechnology.objects.count() == 0:
    print(f"{today} : 생물공학과 첫 크롤링")
    first_crawling(base_url=base_url, url=url, department_model=Biotechnology)
    return
  posts = general_crawling(base_url=base_url, url=url, department_model=Biotechnology)
  
  if len(posts) > 0:
    for post in reversed(posts):
      Biotechnology.objects.create(num=post['num'], title=post['title'])
      isTrue_departments = Department.objects.filter(biotechnology=True)
      isTrue_devices = Device.objects.filter(setting__department__in=isTrue_departments)
      print(f"{today} : 생물공학과 알림 발송")
      pprint.pprint(post)
      send_topic_message("생물공학과", post['title'], isTrue_devices, post['url'], 'bte')
  else:
    print(f"{today} : 생물공학과 새로운 공지 없음")

# 신소재공학부, mse
def materials_science_engineering_crawling():
  today = str(datetime.now())
  base_url = "https://mse.jnu.ac.kr"
  url = 'https://mse.jnu.ac.kr/mse/16863/subview.do'
  if MaterialsScienceEngineering.objects.count() == 0:
    print(f"{today} :  신소재공학부 첫 크롤링")
    first_crawling(base_url=base_url, url=url, department_model=MaterialsScienceEngineering)
    return
  posts = general_crawling(base_url=base_url, url=url, department_model=MaterialsScienceEngineering)
  
  if len(posts) > 0:
    for post in reversed(posts):
      MaterialsScienceEngineering.objects.create(num=post['num'], title=post['title'])
      isTrue_departments = Department.objects.filter(materials_science_engineering=True)
      isTrue_devices = Device.objects.filter(setting__department__in=isTrue_departments)
      print(f"{today} : 신소재공학부 알림 발송")
      pprint.pprint(post)
      send_topic_message("신소재공학부", post['title'], isTrue_devices, post['url'], 'mse')
  else:
    print(f"{today} : 신소재공학부 새로운 공지 없음")

# 소프트웨어공학과, sw
def software_engineering_crawling():
  today = str(datetime.now())
  base_url = "https://sw.jnu.ac.kr"
  url = 'https://sw.jnu.ac.kr/sw/8250/subview.do'
  if SoftwareEngineering.objects.count() == 0:
    print(f"{today} : 소프트웨어공학과 첫 크롤링")
    first_crawling(base_url=base_url, url=url, department_model=SoftwareEngineering)
    return
  posts = general_crawling(base_url=base_url, url=url, department_model=SoftwareEngineering)
  
  if len(posts) > 0:
    for post in reversed(posts):
      SoftwareEngineering.objects.create(num=post['num'], title=post['title'])
      # 소프트웨어공학과를 구독한 User에게 알림 발송
      isTrue_departments = Department.objects.filter(software_engineering=True)
      isTrue_devices = Device.objects.filter(setting__department__in=isTrue_departments)
      print(f"{today} : 소프트웨어공학과 알림 발송")
      pprint.pprint(post)
      send_topic_message("소프트웨어공학과", post['title'], isTrue_devices, post['url'], 'sw')
  else:
    print(f"{today} : 소프트웨어공학과 새로운 공지 없음")