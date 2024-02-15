from django.db import models

## 학과 알림 설정
class DepartmentSet(models.Model):
  ## 간호대학
  nursing = models.BooleanField(default=False) # 간호학과
  ## 경영대학
  biz = models.BooleanField(default=False) # 경영학부
  eco = models.BooleanField(default=False) # 경제학부
  ## 공과대학
  archi = models.BooleanField(default=False) # 건축학부
  pf = models.BooleanField(default=False) # 고분자융합소재공학부
  mech = models.BooleanField(default=False) # 기계공학부
  bte = models.BooleanField(default=False) # 생물공학과
  mse = models.BooleanField(default=False) # 신소재공학부
  resources = models.BooleanField(default=False) # 에너지자원공학과
  ace = models.BooleanField(default=False) # 화학공학부
  elec = models.BooleanField(default=False) # 전기공학과
  ee = models.BooleanField(default=False) # 전자공학과
  ce = models.BooleanField(default=False) # 컴퓨터정보통신공학과
  sw = models.BooleanField(default=False) # 소프트웨어공학과
  civil = models.BooleanField(default=False) # 토목공학과
  eee = models.BooleanField(default=False) # 환경에너지공학과
  ## 농업생명과학대학
  agro = models.BooleanField(default=False) # 응용식물학과
  hort = models.BooleanField(default=False) # 원예생명공학과
  agribio = models.BooleanField(default=False) # 응용생물학과
  forestry = models.BooleanField(default=False) # 산림자원학과
  wood = models.BooleanField(default=False) # 임산공학과
  agrochem = models.BooleanField(default=False) # 농생명화학과
  foodsci = models.BooleanField(default=False) # 식품공학과
  mimb = models.BooleanField(default=False) # 분자생명공학과
  animalscience = models.BooleanField(default=False) # 동물자원학부
  rbe = models.BooleanField(default=False) # 지역·바이오시스템공학과
  ae = models.BooleanField(default=False) # 농업경제학과
  jnula = models.BooleanField(default=False) # 조경학과
  bioenergy = models.BooleanField(default=False) # 바이오에너지공학과
  bse = models.BooleanField(default=False) # 융합바이오시스템기계공학과
  ## 사범대학
  koredu = models.BooleanField(default=False) # 국어교육과
  engedu = models.BooleanField(default=False) # 영어교육과
  educate = models.BooleanField(default=False) # 교육학과
  ecedu = models.BooleanField(default=False) # 유아교육과
  geoedu = models.BooleanField(default=False) # 지리교육과
  hisedu = models.BooleanField(default=False) # 역사교육과
  ethicsedu = models.BooleanField(default=False) # 윤리교육과
  mathedu = models.BooleanField(default=False) # 수학교육과
  physicsedu = models.BooleanField(default=False) # 물리교육과
  chemedu = models.BooleanField(default=False) # 화학교육과
  bioedu = models.BooleanField(default=False) # 생물교육과
  earthedu = models.BooleanField(default=False) # 지구과학교육과
  homeedu = models.BooleanField(default=False) # 가정교육과
  musicedu = models.BooleanField(default=False) # 음악교육과
  physicaledu = models.BooleanField(default=False) # 체육교육과
  spededu = models.BooleanField(default=False) # 특수교육학부
  ## 사회과학대학
  politics = models.BooleanField(default=False) # 정치외교학과
  sociology = models.BooleanField(default=False) # 사회학과
  psyche = models.BooleanField(default=False) # 심리학과
  # list = models.BooleanField(default=False) # 문헌정보학과 > 접속 안됨
  comm = models.BooleanField(default=False) # 신문방송학과
  geo = models.BooleanField(default=False) # 지리학과
  illyu = models.BooleanField(default=False) # 문화인류고고학과
  jnupa = models.BooleanField(default=False) # 행정학과
  ## 생활과학대학
  welfare = models.BooleanField(default=False) # 생활복지학과
  fn = models.BooleanField(default=False) # 식품영양과학부
  clothing = models.BooleanField(default=False) # 의류학과
  ## 예술대학
  fineart = models.BooleanField(default=False) # 미술학과
  music = models.BooleanField(default=False) # 음악학과
  koreanmusic = models.BooleanField(default=False) # 국악학과
  design = models.BooleanField(default=False) # 디자인학과
  ## 인문대학
  korean = models.BooleanField(default=False) # 국어국문학과
  ell = models.BooleanField(default=False) # 영어영문학과
  german = models.BooleanField(default=False) # 독일언어문학과
  french = models.BooleanField(default=False) # 불어불문학과
  china = models.BooleanField(default=False) # 중어중문학과
  nihon = models.BooleanField(default=False) # 일어일문학과
  history = models.BooleanField(default=False) # 사학과
  philos = models.BooleanField(default=False) # 철학과
  ## 자연과학대학
  math = models.BooleanField(default=False) # 수학과
  stat = models.BooleanField(default=False) # 통계학과
  physics = models.BooleanField(default=False) # 물리학과
  geology = models.BooleanField(default=False) # 지질환경전공
  oceanography = models.BooleanField(default=False) # 해양환경전공
  chem = models.BooleanField(default=False) # 화학과
  biology = models.BooleanField(default=False) # 생물학과
  sbst = models.BooleanField(default=False) # 생명과학기술학부
  ## AI융합대학
  aisw = models.BooleanField(default=False) # 인공지능학부
  bigdata = models.BooleanField(default=False) # 빅데이터융합학과
  imob = models.BooleanField(default=False) # 지능형모빌리티융합학과
  ## 자율전공학부
  sdis = models.BooleanField(default=False) # 자율전공학부
  ## 공학대학(여수)
  ece = models.BooleanField(default=False) # 전자통신공학과
  eec = models.BooleanField(default=False) # 전기컴퓨터공학부
  mechse = models.BooleanField(default=False) # 기계시스템공학과
  mechauto = models.BooleanField(default=False) # 기계설계공학과
  mechatronics = models.BooleanField(default=False) # 메카트로닉스공학과
  refri06 = models.BooleanField(default=False) # 냉동공조공학과
  environ = models.BooleanField(default=False) # 환경시스템공학과
  biotech = models.BooleanField(default=False) # 융합생명공학과
  chemeng = models.BooleanField(default=False) # 화공생명공학과
  # adcnu = models.BooleanField(default=False) # 건축디자인학과 > 접속안됨
  # bme = models.BooleanField(default=False) # 의공학과 > 페이지 형태 다름
  # hme = models.BooleanField(default=False) # 핼스케어메디컬공학부 > 페이지 형태 다름
  itce = models.BooleanField(default=False) # 산업기술융합공학과(야간)
  pcme = models.BooleanField(default=False) # 석유화학소재공학과
  smartplant = models.BooleanField(default=False) # 조기취업형 계약학과
  ## 문화사회과학대학(여수)
  inter = models.BooleanField(default=False) # 국제학부
  logistics = models.BooleanField(default=False) # 물류교통학과
  trade = models.BooleanField(default=False) # 국제통상학전공
  dogt = models.BooleanField(default=False) # 글로벌비즈니스학전공
  ccd = models.BooleanField(default=False) # 문화콘텐츠학부
  ctm = models.BooleanField(default=False) # 문화관광경영학과
  ## 수산해양대학(여수)
  engineer = models.BooleanField(default=False) # 기관시스템공학과
  fishpath = models.BooleanField(default=False) # 수산생명의학과
  smartfish = models.BooleanField(default=False) # 스마트수산자원관리학과
  aqua = models.BooleanField(default=False) # 양식생물학과
  oceaneng = models.BooleanField(default=False) # 조선해양공학과
  police = models.BooleanField(default=False) # 해양경찰학과
  marinefs = models.BooleanField(default=False) # 해양바이오식품학과
  marine = models.BooleanField(default=False) # 해양생산관리학과
  ocean89 = models.BooleanField(default=False) # 해양융합과학과
  dfmitl = models.BooleanField(default=False) # 수산해양산업관광레저융합학과(계약학과)
  ## 창의융합학부(여수)
  fcc = models.BooleanField(default=False) # 창의융합학부

class DepartmentPost(models.Model):
  topic = models.TextField()
  num = models.PositiveIntegerField()
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title