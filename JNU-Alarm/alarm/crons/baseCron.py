import requests
from bs4 import BeautifulSoup
import pprint
from urllib3.util.retry import Retry
from ..models import Notification, DepartmentPost

from firebase_admin import messaging

def send_topic_message(title, body, devices, link, topic):
  # See documentation on defining a message payload.
  message = messaging.Message(
      notification=messaging.Notification(
        title=title,
        body=body,
      ),
      topic=topic,
  )
  # Send a message to the devices subscribed to the provided topic.
  response = messaging.send(message)
  # Response is a message ID string.
  print('Successfully sent message:', response)

  for device in devices:
    notifications = Notification.objects.filter(device=device)
    if notifications.count() >= 19:
        # Delete the oldest notification
        oldest_notification = notifications.order_by('created_at').first()
        oldest_notification.delete()

    # Create and save new notification
    Notification.objects.create(device=device, title=title, body=body, link=link)
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

def general_crawling(topic, base_url, bbs_url):
  posts = []
  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"general_crawling() : {topic} http 요청 예외 발생", e)
    return posts
  soup = BeautifulSoup(response.text, 'html.parser')
  last_post = DepartmentPost.objects.filter(topic=topic).last()

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
      print(f"general_crawling() : {topic} 크롤링중 예외 발생", e)
      pass
  return posts


def first_crawling(topic, base_url, bbs_url):
  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"first_crawling() : {topic} http 요청 예외 발생", e)
    return
  soup = BeautifulSoup(response.text, 'html.parser')
  tr = soup.findAll('tr', attrs={'class':''})[1]

  try:
    num = int(tr.find('td', attrs={'class':'td-num'}).text)
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
    DepartmentPost.objects.create(topic=topic, num=post_data['num'], title=post_data['title'])
    print("저장완료")
  except Exception as e:
    print(f"first_crawling() : {topic} 첫 크롤링중 예외 발생", e)
    pass




