import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib3.util.retry import Retry
from .baseCron import UniversityPostData

import smtplib
from email.mime.text import MIMEText

import os, environ
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
      num = int(tr.find('td', attrs={'class':'td-num'}).text)
      td = tr.find('td', attrs={'class':'td-subject'})
      title = td.find('strong').text
      href = td.find('a')['href']
      postUrl = base_url + href
      
      if (num != top_five_posts[repeat_count].num 
          or title != top_five_posts[repeat_count].title 
          or postUrl != top_five_posts[repeat_count].link):
        print(f"{today} : {name} 스캔 결과 문제 발견")
        subject = "⚠️ 전대알림 게시물 스캔 오류 보고"
        content = f"{name} 게시물이 DB와 동일하지 않습니다.\n\n[크롤링 게시물]\nNum: {num}\nTitle: {title}\nLink: {postUrl}\n\n[DB 게시물]\nNum: {top_five_posts[repeat_count].num}\nTitle: {top_five_posts[repeat_count].title}\nLink: {top_five_posts[repeat_count].link}\n"
        send_email(subject, content)
        break
    except Exception as e:
      print(f"general_bbs_scan() : {topic} 크롤링중 예외 발생", e)
      pass
    repeat_count += 1
  print(f"{today} : {name} 스캔 결과 문제 없음")


def send_email(subject, content):
  admin_mail = env('ADMIN_MAIL') # 보안
  admin_password = env('ADMIN_PASSWORD') # 보안

  s = smtplib.SMTP('smtp.gmail.com', 587)  # 세션 생성
  s.starttls()  # TLS 보안 시작
  s.login(admin_mail, admin_password)  # 로그인 인증
  
  # 받는 사람 
  receiver_mail = "dnwls8462@naver.com"

  msg = MIMEText(content)
  msg['Subject'] = subject
  msg['From'] = "전대알림"
  msg['To'] = receiver_mail
  s.sendmail(admin_mail, receiver_mail, msg.as_string())
  s.quit()  # 세션 종료
  print("📧 이메일 발송 완료")