from .baseCron import UniversityPostData, send_topic_message
from ..models import BusinessPost

import requests
from bs4 import BeautifulSoup
import time
import pprint
from urllib3.util.retry import Retry
import re
from datetime import datetime


business_data_list = [
  UniversityPostData(topic='sojoong', base_url="https://www.sojoong.kr/www/notice/view/", bbs_url="https://www.sojoong.kr/www/notice/", name="소프트웨어중심대학사업단"),
  UniversityPostData(topic='aicoss', base_url="https://aicoss.kr/www/notice/view/", bbs_url="https://aicoss.kr/www/notice/?cate=%EC%A0%84%EB%82%A8%EB%8C%80%ED%95%99%EA%B5%90", name="인공지능혁신융합대학사업단"),
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

def sojoong_crawling(topic, base_url, bbs_url, post_model):
  posts = []
  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"sojoong_crawling() : {topic} http 요청 예외 발생", e)
    return posts
  soup = BeautifulSoup(response.text, 'html.parser')
  last_post = post_model.objects.filter(topic=topic).last()
  trs = [tr for tr in soup.find_all('tr') if not tr.find('th')]
  for tr in trs:
    try:
      num = int(re.findall(r'\d+', tr.find('a')['href'])[0])
      if num <= last_post.num:
        continue
      else:
        title = tr.find('strong', attrs={'class':'cutText'}).text
        postUrl = base_url + str(num)
        post_data = {
          'num': num,
          'title': title,
          'url': postUrl
        }
        posts.append(post_data)
    except Exception as e:
      print(f"sojoong_crawling() : {topic} 크롤링중 예외 발생", e)
      pass
  return sorted(posts, key=lambda x: x['num'], reverse=True)

def sojoong_first_crawling(topic, base_url, bbs_url, post_model):
  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"sojoong_first_crawling() : {topic} http 요청 예외 발생", e)
    return
  soup = BeautifulSoup(response.text, 'html.parser')
  trs = [tr for tr in soup.find_all('tr') if not tr.find('th')]
  # 가장 작은 숫자를 찾기 위한 초기값 설정
  max_num = 0
  max_tr_tag = None

  # 각 tr 태그를 순회하며 가장 작은 숫자를 가진 tr 태그 찾기
  for tr in trs:
    num = int(re.findall(r'\d+', tr.find('a')['href'])[0])
    if num > max_num:
      max_num = num
      max_tr_tag = tr

  try:
    if max_tr_tag is not None:
      num = max_num
      title = max_tr_tag.find('strong', attrs={'class':'cutText'}).text
      postUrl = base_url + str(num)
      post_data = {
        'num': num,
        'title': title,
        'url': postUrl
      }
      pprint.pprint(post_data)
      post_model.objects.create(topic=topic, num=post_data['num'], title=post_data['title'], link=post_data['url'])
      print("저장완료")
  except Exception as e:
    print(f"sojoong_first_crawling() : {topic} 첫 크롤링중 예외 발생", e)
    pass

def sojoong_bbs_crawling(post_data: UniversityPostData, post_model):
  today = str(datetime.now())
  topic = post_data.topic
  base_url = post_data.base_url
  bbs_url = post_data.bbs_url
  name = post_data.name
  if post_model.objects.filter(topic=post_data.topic).count() == 0:
    print(f"{today} : {name} 첫 크롤링")
    sojoong_first_crawling(topic=topic, base_url=base_url, bbs_url=bbs_url, post_model=post_model)
    return
  posts = sojoong_crawling(topic=topic, base_url=base_url, bbs_url=bbs_url, post_model=post_model)
  
  if len(posts) > 0:
    for post in reversed(posts):
      post_model.objects.create(topic=topic, num=post['num'], title=post['title'], link=post['url'])
      print(f"{today} : {name} 알림 발송")
      pprint.pprint(post)
      send_topic_message(name, post['title'], post['url'], topic)
      time.sleep(1)
  else:
    print(f"{today} : {name} 새로운 공지 없음")

def business_crawling():
  print("\n> 사업단 크롤링")
  for business_data in business_data_list:
    sojoong_bbs_crawling(post_data=business_data, post_model=BusinessPost)