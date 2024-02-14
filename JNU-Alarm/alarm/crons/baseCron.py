import requests
from bs4 import BeautifulSoup
import pprint

from ..models import Notification

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

def first_crawling(base_url, url, department_model):
  response = requests.get(url)
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
    department_model.objects.create(num=post_data['num'], title=post_data['title'])
  except Exception as e:
    print("첫 크롤링중 예외 발생", e)
    pass




