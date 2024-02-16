from .baseCron import UniversityPostData, send_topic_message
from ..models import HomePost, HomeSet

import requests
from bs4 import BeautifulSoup
import pprint
from urllib3.util.retry import Retry

from datetime import datetime
from ..models import Device


home_data_list = [
  UniversityPostData(topic='academic', base_url="https://www.jnu.ac.kr", bbs_url="https://www.jnu.ac.kr/WebApp/web/HOM/COM/Board/board.aspx?boardID=5&cate=5", name="학사안내"),
  UniversityPostData(topic='scholarship', base_url="https://www.jnu.ac.kr", bbs_url="https://www.jnu.ac.kr/WebApp/web/HOM/COM/Board/board.aspx?boardID=5&cate=8", name="장학안내"),
]

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

def home_crawling(topic, base_url, bbs_url, post_model):
  posts = []
  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"general_crawling() : {topic} http 요청 예외 발생", e)
    return posts
  soup = BeautifulSoup(response.text, 'html.parser')
  last_post = post_model.objects.filter(topic=topic).last()
  all_tr_tags = soup.find_all('tr')
  # class가 비어있는 모든 <tr> 태그를 찾습니다.
  trs = [tr for tr in all_tr_tags if not tr.find('span', class_=True)]
  for tr in trs[1:]:
    try:
      num = int(tr.find('td').find('span').text)
      if num <= last_post.num:
        break
      else:
        title = tr.find('td', attrs={'class':'title'}).find('a').text.replace('\u200b', '').replace('\xa0', ' ')
        href = tr.find('td', attrs={'class':'title'}).find('a')['href']
        postUrl = base_url + href
        post_data = {
          'num': num,
          'title': title,
          'url': postUrl
        }
        posts.append(post_data)
    except Exception as e:
      print(f"home_crawling() : {topic} 크롤링중 예외 발생", e)
      pass
  return posts

def home_first_crawling(topic, base_url, bbs_url, post_model):
  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"home_first_crawling() : {topic} http 요청 예외 발생", e)
    return
  soup = BeautifulSoup(response.text, 'html.parser')
  all_tr_tags = soup.find_all('tr')
  # class가 비어있는 모든 <tr> 태그를 찾습니다.
  trs = [tr for tr in all_tr_tags if not tr.find('span', class_=True)]
  tr = trs[1]
  try:
    num = int(tr.find('td').find('span').text)
    title = tr.find('td', attrs={'class':'title'}).find('a').text.replace('\u200b', '').replace('\xa0', ' ')
    href = tr.find('td', attrs={'class':'title'}).find('a')['href']
    postUrl = base_url + href
    post_data = {
      'num': num,
      'title': title,
      'url': postUrl
    }
    pprint.pprint(post_data)
    post_model.objects.create(topic=topic, num=post_data['num'], title=post_data['title'])
    print("저장완료")
  except Exception as e:
    print(f"home_first_crawling() : {topic} 첫 크롤링중 예외 발생", e)
    pass

def home_bbs_crawling(post_data: UniversityPostData, post_model, set_model):
  today = str(datetime.now())
  topic = post_data.topic
  base_url = post_data.base_url
  bbs_url = post_data.bbs_url
  name = post_data.name
  if post_model.objects.filter(topic=post_data.topic).count() == 0:
    print(f"{today} : {name} 첫 크롤링")
    home_first_crawling(topic=topic, base_url=base_url, bbs_url=bbs_url, post_model=post_model)
    return
  posts = home_crawling(topic=topic, base_url=base_url, bbs_url=bbs_url, post_model=post_model)
  
  if len(posts) > 0:
    for post in reversed(posts):
      post_model.objects.create(topic=topic, num=post['num'], title=post['title'])
      isTrue_department_set = set_model.objects.filter(**{topic: True})
      isTrue_devices = Device.objects.filter(setting__department__in=isTrue_department_set)
      print(f"{today} : {name} 알림 발송")
      pprint.pprint(post)
      send_topic_message(name, post['title'], isTrue_devices, post['url'], topic)
  else:
    print(f"{today} : {name} 새로운 공지 없음")

def homes_crawling():
  print("\n> 홈페이지 크롤링")
  for home_data in home_data_list:
    home_bbs_crawling(post_data=home_data, post_model=HomePost, set_model=HomeSet)