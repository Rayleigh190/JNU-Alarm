import requests
from bs4 import BeautifulSoup
import pprint
from datetime import datetime

from .models import User, Department, SoftwareEngineering

url = 'https://sw.jnu.ac.kr/sw/8250/subview.do'


def my_scheduled_job():
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
        'category':"소프트웨어 공학과",
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
      for user in isTrue_users:
        print(f"{user.id}에게 알림 발송 : {user.fcm_token}")
  else:
    print(f"🖥️ 소프트웨어공학과 새로운 공지 없음 : {today} ")