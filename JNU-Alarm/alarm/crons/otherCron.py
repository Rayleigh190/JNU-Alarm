from .baseCron import UniversityPostData, send_topic_message
from ..models import DepartmentPost
from datetime import datetime
from bs4 import BeautifulSoup
from urllib3.util.retry import Retry
import pprint, time, requests, re

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

# 산업공학과 크롤링
def ie_crawling(topic, base_url, bbs_url, post_model):
  posts = []
  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"ie_crawling() : {topic} http 요청 예외 발생", e)
    return posts
  soup = BeautifulSoup(response.text, 'html.parser')
  last_post = post_model.objects.filter(topic=topic).last()

  for tr in soup.findAll('tr', attrs={'class':['bg1', 'bg2']}):
    try:
      if tr.find('td') is None:
        continue
      num = int(re.search(r'document_srl=([0-9]+)', tr.find('a')['href']).group(1))
      if num <= last_post.num:
        break
      else:
        td = tr.find('td', attrs={'class':'title'})
        title = td.find('a').text
        href = td.find('a')['href']
        postUrl = base_url + href
        post_data = {
          'num': num,
          'title': title,
          'url': postUrl
        }
        posts.append(post_data)
    except Exception as e:
      print(f"ie_crawling() : {topic} 크롤링중 예외 발생", e)
      pass
  return posts

# 산업공학과 첫 크롤링
def ie_first_crawling(topic, base_url, bbs_url, post_model):
  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"ie_first_crawling() : {topic} http 요청 예외 발생", e)
    return
  soup = BeautifulSoup(response.text, 'html.parser')
  tr = soup.findAll('tr', attrs={'class':['bg1', 'bg2']})[0]
  try:
    num = int(re.search(r'document_srl=([0-9]+)', tr.find('a')['href']).group(1))
    td = tr.find('td', attrs={'class':'title'})
    title = td.find('a').text
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
    print(f"ie_first_crawling() : {topic} 첫 크롤링중 예외 발생", e)
    pass

# 산업공학과 게시판 크롤링
def ie_bbs_crawling(post_data: UniversityPostData, post_model):
  today = str(datetime.now())
  topic = post_data.topic
  base_url = post_data.base_url
  bbs_url = post_data.bbs_url
  name = post_data.name
  if post_model.objects.filter(topic=topic).count() == 0:
    print(f"{today} : {name} 첫 크롤링")
    ie_first_crawling(topic=topic, base_url=base_url, bbs_url=bbs_url, post_model=post_model)
    return
  posts = ie_crawling(topic=topic, base_url=base_url, bbs_url=bbs_url, post_model=post_model)

  if len(posts) > 0:
    for post in reversed(posts):
      post_model.objects.create(topic=topic, num=post['num'], title=post['title'], link=post['url'])
      print(f"{today} : {name} 알림 발송")
      pprint.pprint(post)
      send_topic_message(name, post['title'], post['url'], topic)
      time.sleep(1)
  else:
    print(f"{today} : {name} 새로운 공지 없음")

# 산업공학과
ie_post_data = UniversityPostData(topic='ie', base_url="http://ie.jnu.ac.kr", bbs_url="http://ie.jnu.ac.kr/notice", name="산업공학과")

def other_crawling():
  print("\n> 기타 크롤링")
  ie_bbs_crawling(post_data=ie_post_data, post_model=DepartmentPost)