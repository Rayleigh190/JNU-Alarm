import requests
from bs4 import BeautifulSoup
import pprint
import time
from datetime import datetime
from urllib3.util.retry import Retry
from ..models import Notification

from firebase_admin import messaging
from dataclasses import dataclass 


@dataclass 
class UniversityPostData: 
  topic: str
  base_url: str
  bbs_url: str
  name: str
  
def send_topic_message(title, body, link, topic):
  android = messaging.AndroidConfig(
    priority='high',
    notification=messaging.AndroidNotification(
        sound='default',
        channel_id='100',
        priority='high'
    ),
  )

  apns = messaging.APNSConfig(
    payload=messaging.APNSPayload(
      aps=messaging.Aps(
        sound='default',
      )
    )
  )

  message = messaging.Message(
    notification=messaging.Notification(
      title=title,
      body=body,
    ),
    data={
        'title': title,
        'link': link,
    },
    android=android,
    apns=apns,
    topic=topic,
  )
  
  for _ in range(3):
    try:
      response = messaging.send(message)  # 메시지를 전송합니다.
      print('Successfully sent message:', response)
      break  # 성공적으로 메시지를 전송했을 경우 반복문을 종료합니다.
    except Exception as e:  # 전송이 실패할 경우 예외를 처리합니다.
      print('Failed to send message. Retrying...')
      time.sleep(5)  # 5초를 기다린 후 재시도합니다.
  else:
    print('Maximum retry attempts reached. Message could not be sent.')

  Notification.objects.create(topic=topic, title=title, body=body, link=link)
  return

headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-US,en;q=0.9',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4491.0 Safari/537.36'
}

retry_strategy = Retry(total=3)

session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=retry_strategy))
session.mount('https://', requests.adapters.HTTPAdapter(max_retries=retry_strategy))

def general_crawling(topic, base_url, bbs_url, post_model):
  posts = []
  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"general_crawling() : {topic} http 요청 예외 발생", e)
    return posts
  soup = BeautifulSoup(response.text, 'html.parser')
  last_post = post_model.objects.filter(topic=topic).last()

  for tr in soup.findAll('tr', attrs={'class':''}):
    try:
      if tr.find('td') is None:
        continue
      num = int(tr.find('a')['href'].split('/')[4])
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
      print(f"general_crawling() : {topic} 크롤링중 예외 발생", e)
      pass
  return posts

def first_crawling(topic, base_url, bbs_url, post_model):
  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"first_crawling() : {topic} http 요청 예외 발생", e)
    return
  soup = BeautifulSoup(response.text, 'html.parser')
  tr = soup.findAll('tr', attrs={'class':''})[1]

  try:
    num = int(tr.find('a')['href'].split('/')[4])
    td = tr.find('td', attrs={'class':'td-subject'})
    title = td.find('strong').text
    href = td.find('a')['href']
    postUrl = base_url + href
    post_data = {
      'num': num,
      'title': title,
      'url': postUrl
    }
    pprint.pprint(post_data)
    post_model.objects.create(topic=topic, num=post_data['num'], title=post_data['title'], link=post_data['url'])
    print("저장완료")
  except Exception as e:
    print(f"first_crawling() : {topic} 첫 크롤링중 예외 발생", e)
    pass

def general_bbs_crawling(post_data: UniversityPostData, post_model):
  today = str(datetime.now())
  topic = post_data.topic
  base_url = post_data.base_url
  bbs_url = post_data.bbs_url
  name = post_data.name
  if post_model.objects.filter(topic=post_data.topic).count() == 0:
    print(f"{today} : {name} 첫 크롤링")
    first_crawling(topic=topic, base_url=base_url, bbs_url=bbs_url, post_model=post_model)
    return
  posts = general_crawling(topic=topic, base_url=base_url, bbs_url=bbs_url, post_model=post_model)
  
  if len(posts) > 0:
    for post in reversed(posts):
      post_model.objects.create(topic=topic, num=post['num'], title=post['title'], link=post['url'])
      print(f"{today} : {name} 알림 발송")
      pprint.pprint(post)
      send_topic_message(name, post['title'], post['url'], topic)
      time.sleep(1)
  else:
    print(f"{today} : {name} 새로운 공지 없음")


