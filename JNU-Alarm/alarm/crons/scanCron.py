import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib3.util.retry import Retry
from .baseCron import UniversityPostData
from ..models import Notification

from .asynchronous_send_mail import send_mail
from django.conf import settings
import os, environ, re
from pathlib import Path

# env 파일 불러오기 Start
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# env 파일 불러오기 End

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


# 실제 게시물과 DB의 저장된 게시물의 동일함을 확인합니다.
def general_bbs_scan(post_data: UniversityPostData, post_model):
  today = str(datetime.now())
  topic = post_data.topic
  base_url = post_data.base_url
  bbs_url = post_data.bbs_url
  name = post_data.name

  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"general_bbs_scan() : {topic} http 요청 예외 발생", e)
  soup = BeautifulSoup(response.text, 'html.parser')

  top_five_posts = post_model.objects.filter(topic=topic).order_by('-id')[:5]

  repeat_count = 0
  # 게시물 번호, 제목, 링크를 DB에 저장 된 것과 비교 합니다.
  for tr in soup.findAll('tr', attrs={'class':''}):
    if repeat_count > len(top_five_posts)-1: break # 상위 5개 게시물만 확인 합니다.
    try:
      if tr.find('td') is None:
        continue
      num = int(tr.find('a')['href'].split('/')[4])
      td = tr.find('td', attrs={'class':'td-subject'})
      title = td.find('strong').text
      href = td.find('a')['href']
      postUrl = base_url + href

      post = top_five_posts[repeat_count]
      repeat_count += 1  # 위치 중요합니다.

      num_state = num != post.num 
      title_state = title != post.title 
      link_state = postUrl != post.link

      if not num_state and not link_state and title_state:
        previous_title = post.title
        print(f"{today} : {name} 스캔 결과 문제 발견")
        print("Title을 변경 합니다.")
        print(f"From: {previous_title}")
        print(f"To: {title}")
        post.title = title
        post.save()
        
        # 알림내역 body 수정 START
        notification = Notification.objects.get(link=post.link)
        notification.body = title
        notification.save()
        # 알림내역 body 수정 END

        subject = "🛠️ 전대알림 게시물 데이터 수정 보고"
        content = f'''{name} 게시물의 데이터가 수정 되었습니다.\n
From: {previous_title} > To: {title}\n
Topic: {topic}
상태: Num({not num_state}), Title({not title_state}), Link({not link_state})\n
[크롤링 게시물]
Num: {num}
Title: {title}
Link: {postUrl}\n
[DB 게시물]
Num: {post.num}
Title: {previous_title}
Link: {post.link}\n'''
        send_email(subject, content)
        continue

      if (num_state or title_state or link_state):
        print(f"{today} : {name} 스캔 결과 문제 발견")
        subject = "⚠️ 전대알림 게시물 스캔 오류 보고"
        content = f'''{name} 게시물이 DB와 동일하지 않습니다.\n
Topic: {topic}
상태: Num({not num_state}), Title({not title_state}), Link({not link_state})\n
[크롤링 게시물]
Num: {num}
Title: {title}
Link: {postUrl}\n
[DB 게시물]
Num: {post.num}
Title: {post.title}
Link: {post.link}\n'''
        send_email(subject, content)
        break
    except Exception as e:
      print(f"general_bbs_scan() : {topic} 크롤링중 예외 발생", e)
      pass
  print(f"{today} : {name} 스캔 결과 문제 없음")


def home_bbs_scan(post_data: UniversityPostData, post_model):
  today = str(datetime.now())
  topic = post_data.topic
  base_url = post_data.base_url
  bbs_url = post_data.bbs_url
  name = post_data.name

  try:
    response = session.get(bbs_url, headers=headers)
  except Exception as e:
    print(f"home_bbs_scan() : {topic} http 요청 예외 발생", e)
    return
  soup = BeautifulSoup(response.text, 'html.parser')

  top_five_posts = post_model.objects.filter(topic=topic).order_by('-id')[:5] # DB에서 가져온 게시물들

  all_tr_tags = soup.find_all('tr')

  posts = []  # 게시판에서 가져온 게시물들
  # 게시판에서 글들을 가져와 num 기준 내림차순으로 정렬합니다.
  for tr in all_tr_tags[1:]:
    try:
      num = int(re.findall(r'key=(\d+)', tr.find('a')['href'])[0])
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
      print(f"home_bbs_scan() : {topic} 크롤링중 예외 발생", e)
      pass
  posts.sort(key=lambda x: x['num'], reverse=True)

  for i, post in enumerate(top_five_posts):
    num_state = posts[i]['num'] != post.num 
    title_state = posts[i]['title'] != post.title 
    link_state = posts[i]['url'] != post.link

    if not num_state and not link_state and title_state:
      previous_title = post.title
      new_title = posts[i]['title']
      print(f"{today} : {name} 스캔 결과 문제 발견")
      print("Title을 변경 합니다.")
      print(f"From: {previous_title}")
      print(f"To: {new_title}")
      post.title = new_title
      post.save()
      
      # 알림내역 body 수정 START
      notification = Notification.objects.get(link=post.link)
      notification.body = new_title
      notification.save()
      # 알림내역 body 수정 END

      subject = "🛠️ 전대알림 게시물 데이터 수정 보고"
      content = f'''{name} 게시물의 데이터가 수정 되었습니다.\n
From: {previous_title} > To: {new_title}\n
Topic: {topic}
상태: Num({not num_state}), Title({not title_state}), Link({not link_state})\n
[크롤링 게시물]
Num: {posts[i]['num']}
Title: {new_title}
Link: {posts[i]['url']}\n
[DB 게시물]
Num: {post.num}
Title: {previous_title}
Link: {post.link}\n'''
      send_email(subject, content)
      continue

    if (num_state or title_state or link_state):
      print(f"{today} : {name} 스캔 결과 문제 발견")
      subject = "⚠️ 전대알림 게시물 스캔 오류 보고"
      content = f'''{name} 게시물이 DB와 동일하지 않습니다.\n
Topic: {topic}
상태: Num({not num_state}), Title({not title_state}), Link({not link_state})\n
[크롤링 게시물]
Num: {posts[i]['num']}
Title: {posts[i]['title']}
Link: {posts[i]['url']}\n
[DB 게시물]
Num: {post.num}
Title: {post.title}
Link: {post.link}\n'''
      send_email(subject, content)
      break
  print(f"{today} : {name} 스캔 결과 문제 없음")


def send_email(subject, content):
  try:
    receiver_email = "dnwls8462@naver.com"
    send_mail(
        subject=subject,
        body=content,
        from_email=f'전대알림 <{settings.EMAIL_HOST_USER}>',
        recipient_list=[receiver_email],
        auth_user="전대알림",
    )
    print("📧 이메일 발송")
  except Exception as e:
    print(f"이메일 발송 오류 발생 : {e}")