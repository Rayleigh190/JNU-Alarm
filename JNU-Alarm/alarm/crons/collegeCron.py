import pprint
from datetime import datetime
from .baseCron import general_crawling, first_crawling, send_topic_message

from ..models import Device, College, Engineering


## 대학
# 공과대학, eng
def engineering_crawling():
  today = str(datetime.now())
  base_url = "https://eng.jnu.ac.kr"
  url = 'https://eng.jnu.ac.kr/eng/7343/subview.do'
  if Engineering.objects.count() == 0:
    print(f"{today} : 공과대학 첫 크롤링")
    first_crawling(base_url=base_url, url=url, department_model=Engineering)
    return
  posts = general_crawling(base_url=base_url, url=url, department_model=Engineering)
  
  if len(posts) > 0:
    for post in reversed(posts):
      Engineering.objects.create(num=post['num'], title=post['title'])
      # 공과대학을 구독한 User에게 알림 발송
      isTrue_college =College.objects.filter(engineering=True)
      isTrue_devices = Device.objects.filter(setting__college__in=isTrue_college)
      print(f"{today} : 공과대학 알림 발송")
      pprint.pprint(post)
      send_topic_message("공과대학", post['title'], isTrue_devices, post['url'], 'eng')
  else:
    print(f"{today} : 공과대학 새로운 공지 없음")