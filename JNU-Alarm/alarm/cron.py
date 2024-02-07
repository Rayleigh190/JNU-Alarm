import requests
from bs4 import BeautifulSoup
import pprint
from datetime import datetime

from .models import User, Notification
from .models import Department, Architecture, SoftwareEngineering
from .models import College, Engineering

def send_message(title, body, users, link):
  for user in users:
    Notification.objects.create(user=user, category=title, title=body, link=link)
  print(f"pushed to {users}")
  return

def crawling_job():
  architecture_crawling()
  software_engineering_crawling()
  engineering_crawling()

def general_crawling(base_url, url, department_model):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  posts = []
  last_post = department_model.objects.last()
  for tr in soup.findAll('tr', attrs={'class':''}):
    try:
      if tr.find('td') is None:
        continue
      num = int(tr.find('td', attrs={'class':'td-num'}).text)
      if num <= last_post.num:
        break
      else:
        td = tr.find('td', attrs={'class':'td-subject'})
        title = td.find('strong').text
        href = td.find('a')['href']
        postUrl = base_url + href
        post_data = {
          'num': num,
          'title': title,
          'url': postUrl
        }
        posts.append(post_data)
    except Exception as e:
      print("크롤링중 예외 발생", e)
      pass
  return posts

## 학과 클롤링
# 건축학부
def architecture_crawling():
  today = str(datetime.now())
  base_url = "https://archi.jnu.ac.kr"
  url = 'https://archi.jnu.ac.kr/archi/8023/subview.do'
  posts = general_crawling(base_url=base_url, url=url, department_model=Architecture)
  
  if len(posts) > 0:
    for post in reversed(posts):
      Architecture.objects.create(num=post['num'], title=post['title'])
      isTrue_departments = Department.objects.filter(architecture=True)
      isTrue_users = User.objects.filter(setting__department__in=isTrue_departments)
      send_message("건축학부", post['title'], isTrue_users, post['url'])
      print(f"🏠 건축학부 알림 발송 : {today} ")
      pprint.pprint(post)
  else:
    print(f"🏠 건축학부 새로운 공지 없음 : {today} ")

# 소프트웨어공학과
def software_engineering_crawling():
  today = str(datetime.now())
  base_url = "https://sw.jnu.ac.kr"
  url = 'https://sw.jnu.ac.kr/sw/8250/subview.do'
  posts = general_crawling(base_url=base_url, url=url, department_model=SoftwareEngineering)
  
  if len(posts) > 0:
    for post in reversed(posts):
      SoftwareEngineering.objects.create(num=post['num'], title=post['title'])
      # 소프트웨어공학과를 구독한 User에게 알림 발송
      isTrue_departments = Department.objects.filter(software_engineering=True)
      isTrue_users = User.objects.filter(setting__department__in=isTrue_departments)
      send_message("소프트웨어공학과", post['title'], isTrue_users, post['url'])
      print(f"💻 소프트웨어공학과 알림 발송 : {today} ")
      pprint.pprint(post)
  else:
    print(f"💻 소프트웨어공학과 새로운 공지 없음 : {today} ")

# 공과대학
def engineering_crawling():
  today = str(datetime.now())
  base_url = "https://eng.jnu.ac.kr"
  url = 'https://eng.jnu.ac.kr/eng/7343/subview.do'
  posts = general_crawling(base_url=base_url, url=url, department_model=Engineering)
  
  if len(posts) > 0:
    for post in reversed(posts):
      Engineering.objects.create(num=post['num'], title=post['title'])
      # 공과대학을 구독한 User에게 알림 발송
      isTrue_college =College.objects.filter(engineering=True)
      isTrue_users = User.objects.filter(setting__college__in=isTrue_college)
      send_message("공과대학", post['title'], isTrue_users, post['url'])
      print(f"🛠️ 공과대학 알림 발송 : {today} ")
      pprint.pprint(post)
  else:
    print(f"🛠️ 공과대학 새로운 공지 없음 : {today} ")