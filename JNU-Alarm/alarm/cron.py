import requests
from bs4 import BeautifulSoup
import pprint
from datetime import datetime

from .models import User, Notification, Department, SoftwareEngineering
from .models import College, Engineering

def send_message(title, body, users, link):
  for user in users:
    Notification.objects.create(user=user, category=title, title=body, link=link)
  print(f"pushed to {users}")
  return

def crawling_job():
  software_engineering_crawling()
  engineering_crawling()

# 소프트웨어공학과
def software_engineering_crawling():
  url = 'https://sw.jnu.ac.kr/sw/8250/subview.do'
  today = str(datetime.now())
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  posts = []
  last_post = SoftwareEngineering.objects.last()
  for tr in soup.findAll('tr', attrs={'class':''}):
    try:
      td = tr.find('td', attrs={'class':'td-subject'})
      title = td.find('strong').text
      href = td.find('a')['href']
      postUrl = "https://sw.jnu.ac.kr/"+href
      post_data = {
        'category':"소프트웨어공학과",
        'title': title,
        'url': postUrl
      }
      if title == last_post.title:
        break
      else:
        posts.append(post_data)
    except:
      pass
  
  if len(posts) > 0:
    for post in reversed(posts):
      SoftwareEngineering.objects.create(title=post['title'])
      # 소프트웨어공학과를 구독한 User에게 알림 발송
      isTrue_departments = Department.objects.filter(software_engineering=True)
      isTrue_users = User.objects.filter(setting__department__in=isTrue_departments)
      print(f"🖥️ 소프트웨어공학과 알림 발송 : {today} ")
      pprint.pprint(post)
      send_message(post['category'], post['title'], isTrue_users, post['url'])
  else:
    print(f"🖥️ 소프트웨어공학과 새로운 공지 없음 : {today} ")

# 공과대학
def engineering_crawling():
  url = 'https://eng.jnu.ac.kr/eng/7343/subview.do'
  today = str(datetime.now())
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  posts = []
  last_post = Engineering.objects.last()
  for tr in soup.findAll('tr', attrs={'class':''}):
    try:
      td = tr.find('td', attrs={'class':'td-subject'})
      title = td.find('strong').text
      href = td.find('a')['href']
      postUrl = "https://eng.jnu.ac.kr/"+href
      post_data = {
        'category':"공과대학",
        'title': title,
        'url': postUrl
      }
      if title == last_post.title:
        break
      else:
        posts.append(post_data)
    except:
      pass
  
  if len(posts) > 0:
    for post in reversed(posts):
      Engineering.objects.create(title=post['title'])
      # 공과대학을 구독한 User에게 알림 발송
      isTrue_college =College.objects.filter(engineering=True)
      isTrue_users = User.objects.filter(setting__college__in=isTrue_college)
      print(f"🔨 공과대학 알림 발송 : {today} ")
      pprint.pprint(post)
      send_message(post['category'], post['title'], isTrue_users, post[url])
  else:
    print(f"🔨 공과대학 새로운 공지 없음 : {today} ")