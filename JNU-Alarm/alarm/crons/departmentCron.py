from .baseCron import general_bbs_crawling, UniversityPostData
from ..models import DepartmentSet, DepartmentPost

department_data_list = [
  ## 간호대학
  UniversityPostData(topic='nursing', base_url="https://nursing.jnu.ac.kr", bbs_url="https://nursing.jnu.ac.kr/nursing/5656/subview.do", name="간호학과"),
  ## 경영대학
  UniversityPostData(topic='biz', base_url="https://biz.jnu.ac.kr", bbs_url="https://biz.jnu.ac.kr/biz/12212/subview.do", name="경영학부"),
  UniversityPostData(topic='eco', base_url="https://eco.jnu.ac.kr", bbs_url="https://eco.jnu.ac.kr/eco/12253/subview.do", name="경제학부"),
  ## 공과대학
  UniversityPostData(topic='archi', base_url="https://archi.jnu.ac.kr", bbs_url="https://archi.jnu.ac.kr/archi/8023/subview.do", name="건축학부"),
  UniversityPostData(topic='pf', base_url="https://pf.jnu.ac.kr", bbs_url="https://pf.jnu.ac.kr/pf/7821/subview.do", name="고분자융합소재공학부"),
  UniversityPostData(topic='mech', base_url="https://mech.jnu.ac.kr", bbs_url="https://mech.jnu.ac.kr/mech/8218/subview.do", name="기계공학부"),
  UniversityPostData(topic='bte', base_url="https://bte.jnu.ac.kr", bbs_url="https://bte.jnu.ac.kr/bte/10981/subview.do", name="생물공학과"),
  UniversityPostData(topic='mse', base_url="https://mse.jnu.ac.kr", bbs_url="https://mse.jnu.ac.kr/mse/16863/subview.do", name="신소재공학부"),
  UniversityPostData(topic='resources', base_url="https://resources.jnu.ac.kr", bbs_url="https://resources.jnu.ac.kr/resources/14018/subview.do", name="에너지자원공학과"),
  UniversityPostData(topic='ace', base_url="https://ace.jnu.ac.kr", bbs_url="https://ace.jnu.ac.kr/ace/12509/subview.do", name="화학공학부"),
  UniversityPostData(topic='elec', base_url="https://elec.jnu.ac.kr", bbs_url="https://elec.jnu.ac.kr/elec/14099/subview.do", name="전기공학과"),
  UniversityPostData(topic='ee', base_url="https://ee.jnu.ac.kr", bbs_url="https://ee.jnu.ac.kr/ee/12439/subview.do", name="전자공학과"),
  UniversityPostData(topic='ce', base_url="https://ce.jnu.ac.kr", bbs_url="https://ce.jnu.ac.kr/ce/12474/subview.do", name="컴퓨터정보통신공학과"),
  UniversityPostData(topic='sw', base_url="https://sw.jnu.ac.kr", bbs_url="https://sw.jnu.ac.kr/sw/8250/subview.do", name="소프트웨어공학과"),
  UniversityPostData(topic='civil', base_url="https://civil.jnu.ac.kr", bbs_url="https://civil.jnu.ac.kr/civil/11107/subview.do", name="토목공학과"),
  UniversityPostData(topic='eee', base_url="https://eee.jnu.ac.kr", bbs_url="https://eee.jnu.ac.kr/eee/11181/subview.do", name="환경에너지공학과"),
  ## 농업생명과학대학
  UniversityPostData(topic='agro', base_url="https://agro.jnu.ac.kr", bbs_url="https://agro.jnu.ac.kr/agro/4810/subview.do", name="응용식물학과"),
  UniversityPostData(topic='hort', base_url="https://hort.jnu.ac.kr", bbs_url="https://hort.jnu.ac.kr/hort/5820/subview.do", name="원예생명공학과"),
  UniversityPostData(topic='agribio', base_url="https://agribio.jnu.ac.kr", bbs_url="https://agribio.jnu.ac.kr/agribio/5396/subview.do", name="응용생물학과"),
  UniversityPostData(topic='forestry', base_url="https://forestry.jnu.ac.kr", bbs_url="https://forestry.jnu.ac.kr/forestry/4751/subview.do", name="산림자원학과"),
  UniversityPostData(topic='wood', base_url="https://wood.jnu.ac.kr", bbs_url="https://wood.jnu.ac.kr/wood/5487/subview.do", name="임산공학과"),
  UniversityPostData(topic='agrochem', base_url="https://agrochem.jnu.ac.kr", bbs_url="https://agrochem.jnu.ac.kr/agrochem/5247/subview.do", name="농생명화학과"),
  UniversityPostData(topic='foodsci', base_url="https://foodsci.jnu.ac.kr", bbs_url="https://foodsci.jnu.ac.kr/foodsci/5596/subview.do", name="식품공학과"),
  UniversityPostData(topic='mimb', base_url="https://mimb.jnu.ac.kr", bbs_url="https://mimb.jnu.ac.kr/mimb/5348/subview.do", name="분자생명공학과"),
  UniversityPostData(topic='animalscience', base_url="https://animalscience.jnu.ac.kr", bbs_url="https://animalscience.jnu.ac.kr/animalscience/4725/subview.do", name="동물자원학부"),
  UniversityPostData(topic='rbe', base_url="https://rbe.jnu.ac.kr", bbs_url="https://rbe.jnu.ac.kr/rbe/4855/subview.do", name="지역·바이오시스템공학과"),
  UniversityPostData(topic='ae', base_url="https://ae.jnu.ac.kr", bbs_url="https://ae.jnu.ac.kr/ae/4699/subview.do", name="농업경제학과"),
  UniversityPostData(topic='jnula', base_url="https://jnula.jnu.ac.kr", bbs_url="https://jnula.jnu.ac.kr/jnula/5562/subview.do", name="조경학과"),
  UniversityPostData(topic='bioenergy', base_url="https://bioenergy.jnu.ac.kr", bbs_url="https://bioenergy.jnu.ac.kr/bioenergy/19179/subview.do", name="바이오에너지공학과"),
  UniversityPostData(topic='bse', base_url="https://bse.jnu.ac.kr", bbs_url="https://bse.jnu.ac.kr/bse/16824/subview.do", name="융합바이오시스템기계공학과"),
  ## 사범대학
  UniversityPostData(topic='koredu', base_url="https://koredu.jnu.ac.kr", bbs_url="https://koredu.jnu.ac.kr/koredu/15485/subview.do", name="국어교육과"),
  UniversityPostData(topic='engedu', base_url="https://engedu.jnu.ac.kr", bbs_url="https://engedu.jnu.ac.kr/engedu/15551/subview.do", name="영어교육과"),
  UniversityPostData(topic='educate', base_url="https://educate.jnu.ac.kr", bbs_url="https://educate.jnu.ac.kr/educate/15423/subview.do", name="교육학과"),
  UniversityPostData(topic='ecedu', base_url="https://ecedu.jnu.ac.kr", bbs_url="https://ecedu.jnu.ac.kr/ecedu/15739/subview.do", name="유아교육과"),
  UniversityPostData(topic='geoedu', base_url="https://geoedu.jnu.ac.kr", bbs_url="https://geoedu.jnu.ac.kr/geoedu/15675/subview.do", name="지리교육과"),
  UniversityPostData(topic='hisedu', base_url="https://hisedu.jnu.ac.kr", bbs_url="https://hisedu.jnu.ac.kr/hisedu/15619/subview.do", name="역사교육과"),
  UniversityPostData(topic='ethicsedu', base_url="https://ethicsedu.jnu.ac.kr", bbs_url="https://ethicsedu.jnu.ac.kr/ethicsedu/15801/subview.do", name="윤리교육과"),
  UniversityPostData(topic='mathedu', base_url="https://mathedu.jnu.ac.kr", bbs_url="https://mathedu.jnu.ac.kr/mathedu/15864/subview.do", name="수학교육과"),
  UniversityPostData(topic='physicsedu', base_url="https://physicsedu.jnu.ac.kr", bbs_url="https://physicsedu.jnu.ac.kr/physicsedu/15930/subview.do", name="물리교육과"),
  UniversityPostData(topic='chemedu', base_url="https://chemedu.jnu.ac.kr", bbs_url="https://chemedu.jnu.ac.kr/chemedu/15994/subview.do", name="화학교육과"),
  UniversityPostData(topic='bioedu', base_url="https://bioedu.jnu.ac.kr", bbs_url="https://bioedu.jnu.ac.kr/bioedu/16060/subview.do", name="생물교육과"),
  UniversityPostData(topic='earthedu', base_url="https://earthedu.jnu.ac.kr", bbs_url="https://earthedu.jnu.ac.kr/earthedu/16116/subview.do", name="지구과학교육과"),
  UniversityPostData(topic='homeedu', base_url="https://homeedu.jnu.ac.kr", bbs_url="https://homeedu.jnu.ac.kr/homeedu/16174/subview.do", name="가정교육과"),
  UniversityPostData(topic='musicedu', base_url="https://musicedu.jnu.ac.kr", bbs_url="https://musicedu.jnu.ac.kr/musicedu/16241/subview.do", name="음악교육과"),
  UniversityPostData(topic='physicaledu', base_url="https://physicaledu.jnu.ac.kr", bbs_url="https://physicaledu.jnu.ac.kr/physicaledu/16292/subview.do", name="체육교육과"),
  UniversityPostData(topic='spededu', base_url="https://spededu.jnu.ac.kr", bbs_url="https://spededu.jnu.ac.kr/spededu/16350/subview.do", name="특수교육학부"),
  ## 사회과학대학
  UniversityPostData(topic='politics', base_url="https://politics.jnu.ac.kr", bbs_url="https://politics.jnu.ac.kr/politics/14165/subview.do", name="정치외교학과"),
  UniversityPostData(topic='sociology', base_url="https://sociology.jnu.ac.kr", bbs_url="https://sociology.jnu.ac.kr/sociology/8677/subview.do", name="사회학과"),
  UniversityPostData(topic='psyche', base_url="https://psyche.jnu.ac.kr", bbs_url="https://psyche.jnu.ac.kr/psyche/9173/subview.do", name="심리학과"),
  UniversityPostData(topic='comm', base_url="https://comm.jnu.ac.kr", bbs_url="https://comm.jnu.ac.kr/comm/8720/subview.do", name="신문방송학과"),
  UniversityPostData(topic='geo', base_url="https://geo.jnu.ac.kr", bbs_url="https://geo.jnu.ac.kr/geo/12730/subview.do", name="지리학과"),
  UniversityPostData(topic='illyu', base_url="https://illyu.jnu.ac.kr", bbs_url="https://illyu.jnu.ac.kr/illyu/12696/subview.do", name="문화인류고고학과"),
  UniversityPostData(topic='jnupa', base_url="https://jnupa.jnu.ac.kr", bbs_url="https://jnupa.jnu.ac.kr/jnupa/14210/subview.do", name="행정학과"),
  ## 생활과학대학
  UniversityPostData(topic='welfare', base_url="https://welfare.jnu.ac.kr", bbs_url="https://welfare.jnu.ac.kr/welfare/11249/subview.do", name="생활복지학과"),
  UniversityPostData(topic='fn', base_url="https://fn.jnu.ac.kr", bbs_url="https://fn.jnu.ac.kr/fn/16376/subview.do", name="식품영양과학부"),
  UniversityPostData(topic='clothing', base_url="https://clothing.jnu.ac.kr", bbs_url="https://clothing.jnu.ac.kr/clothing/9215/subview.do", name="의류학과"),
  ## 예술대학
  UniversityPostData(topic='fineart', base_url="https://fineart.jnu.ac.kr", bbs_url="https://fineart.jnu.ac.kr/fineart/9295/subview.do", name="미술학과"),
  UniversityPostData(topic='music', base_url="https://music.jnu.ac.kr", bbs_url="https://music.jnu.ac.kr/music/8909/subview.do", name="음악학과"),
  UniversityPostData(topic='koreanmusic', base_url="https://koreanmusic.jnu.ac.kr", bbs_url="https://koreanmusic.jnu.ac.kr/koreanmusic/14242/subview.do", name="국악학과"),
  UniversityPostData(topic='design', base_url="https://design.jnu.ac.kr", bbs_url="https://design.jnu.ac.kr/design/9252/subview.do", name="디자인학과"),
  ## 인문대학
  UniversityPostData(topic='korean', base_url="https://korean.jnu.ac.kr", bbs_url="https://korean.jnu.ac.kr/korean/14279/subview.do", name="국어국문학과"),
  UniversityPostData(topic='ell', base_url="https://ell.jnu.ac.kr", bbs_url="https://ell.jnu.ac.kr/ell/14392/subview.do", name="영어영문학과"),
  UniversityPostData(topic='german', base_url="https://german.jnu.ac.kr", bbs_url="https://german.jnu.ac.kr/german/14312/subview.do", name="독일언어문학과"),
  UniversityPostData(topic='french', base_url="https://french.jnu.ac.kr", bbs_url="https://french.jnu.ac.kr/french/13031/subview.do", name="불어불문학과"),
  UniversityPostData(topic='china', base_url="https://china.jnu.ac.kr", bbs_url="https://china.jnu.ac.kr/china/14445/subview.do", name="중어중문학과"),
  UniversityPostData(topic='nihon', base_url="https://nihon.jnu.ac.kr", bbs_url="https://nihon.jnu.ac.kr/nihon/10686/subview.do", name="일어일문학과"),
  UniversityPostData(topic='history', base_url="https://history.jnu.ac.kr", bbs_url="https://history.jnu.ac.kr/history/14361/subview.do", name="사학과"),
  UniversityPostData(topic='philos', base_url="https://philos.jnu.ac.kr", bbs_url="https://philos.jnu.ac.kr/philos/13081/subview.do", name="철학과"),
  ## 자연과학대학
  UniversityPostData(topic='math', base_url="https://math.jnu.ac.kr", bbs_url="https://math.jnu.ac.kr/math/13253/subview.do", name="수학과"),
  UniversityPostData(topic='stat', base_url="https://stat.jnu.ac.kr", bbs_url="https://stat.jnu.ac.kr/stat/8951/subview.do", name="통계학과"),
  UniversityPostData(topic='physics', base_url="https://physics.jnu.ac.kr", bbs_url="https://physics.jnu.ac.kr/physics/13131/subview.do", name="물리학과"),
  UniversityPostData(topic='geology', base_url="https://geology.jnu.ac.kr", bbs_url="https://geology.jnu.ac.kr/geology/10783/subview.do", name="지질환경전공"),
  UniversityPostData(topic='oceanography', base_url="https://oceanography.jnu.ac.kr", bbs_url="https://oceanography.jnu.ac.kr/oceanography/13327/subview.do", name="해양환경전공"),
  UniversityPostData(topic='chem', base_url="https://chem.jnu.ac.kr", bbs_url="https://chem.jnu.ac.kr/chem/10822/subview.do", name="화학과"),
  UniversityPostData(topic='biology', base_url="https://biology.jnu.ac.kr", bbs_url="https://biology.jnu.ac.kr/biology/18020/subview.do", name="생물학과"),
  UniversityPostData(topic='sbst', base_url="https://sbst.jnu.ac.kr", bbs_url="https://sbst.jnu.ac.kr/sbst/9887/subview.do", name="생명과학기술학부"),
  ## AI융합대학
  UniversityPostData(topic='aisw', base_url="https://aisw.jnu.ac.kr", bbs_url="https://aisw.jnu.ac.kr/aisw/518/subview.do", name="인공지능학부"),
  UniversityPostData(topic='bigdata', base_url="https://bigdata.jnu.ac.kr", bbs_url="https://bigdata.jnu.ac.kr/bigdata/472/subview.do", name="빅데이터융합학과"),
  UniversityPostData(topic='imob', base_url="https://imob.jnu.ac.kr", bbs_url="https://imob.jnu.ac.kr/imob/498/subview.do", name="지능형모빌리티융합학과"),
  ## 자율전공학부
  UniversityPostData(topic='sdis', base_url="https://sdis.jnu.ac.kr", bbs_url="https://sdis.jnu.ac.kr/sdis/1950/subview.do", name="자율전공학부"),
  ## 공학대학(여수)
  UniversityPostData(topic='ece', base_url="https://ece.jnu.ac.kr", bbs_url="https://ece.jnu.ac.kr/ece/17724/subview.do", name="전자통신공학과"),
  UniversityPostData(topic='eec', base_url="https://eec.jnu.ac.kr", bbs_url="https://eec.jnu.ac.kr/eec/18203/subview.do", name="전기컴퓨터공학부"),
  UniversityPostData(topic='mechse', base_url="https://mechse.jnu.ac.kr", bbs_url="https://mechse.jnu.ac.kr/mechse/17770/subview.do", name="기계시스템공학과"),
  UniversityPostData(topic='mechauto', base_url="https://mechauto.jnu.ac.kr", bbs_url="https://mechauto.jnu.ac.kr/mechauto/3117/subview.do", name="기계설계공학과"),
  UniversityPostData(topic='mechatronics', base_url="https://mechatronics.jnu.ac.kr", bbs_url="https://mechatronics.jnu.ac.kr/mechatronics/17749/subview.do", name="메카트로닉스공학과"),
  UniversityPostData(topic='refri06', base_url="https://refri06.jnu.ac.kr", bbs_url="https://refri06.jnu.ac.kr/refri06/878/subview.do", name="냉동공조공학과"),
  UniversityPostData(topic='environ', base_url="https://environ.jnu.ac.kr", bbs_url="https://environ.jnu.ac.kr/environ/2962/subview.do", name="환경시스템공학과"),
  UniversityPostData(topic='biotech', base_url="https://biotech.jnu.ac.kr", bbs_url="https://biotech.jnu.ac.kr/biotech/1138/subview.do", name="융합생명공학과"),
  UniversityPostData(topic='chemeng', base_url="https://chemeng.jnu.ac.kr", bbs_url="https://chemeng.jnu.ac.kr/chemeng/2026/subview.do", name="화공생명공학과"),
  UniversityPostData(topic='itce', base_url="https://itce.jnu.ac.kr", bbs_url="https://itce.jnu.ac.kr/itce/3331/subview.do", name="산업기술융합공학과(야간)"),
  UniversityPostData(topic='pcme', base_url="https://pcme.jnu.ac.kr", bbs_url="https://pcme.jnu.ac.kr/pcme/318/subview.do", name="석유화학소재공학과"),
  UniversityPostData(topic='smartplant', base_url="https://smartplant.jnu.ac.kr", bbs_url="https://smartplant.jnu.ac.kr/smartplant/3276/subview.do", name="조기취업형 계약학과"),
  ## 문화사회과학대학(여수)
  UniversityPostData(topic='inter', base_url="https://inter.jnu.ac.kr", bbs_url="https://inter.jnu.ac.kr/inter/1825/subview.do", name="국제학부"),
  UniversityPostData(topic='logistics', base_url="https://logistics.jnu.ac.kr", bbs_url="https://logistics.jnu.ac.kr/logistics/1803/subview.do", name="물류교통학과"),
  UniversityPostData(topic='trade', base_url="https://trade.jnu.ac.kr", bbs_url="https://trade.jnu.ac.kr/trade/2541/subview.do", name="국제통상학전공"),
  UniversityPostData(topic='dogt', base_url="https://dogt.jnu.ac.kr", bbs_url="https://dogt.jnu.ac.kr/dogt/2727/subview.do", name="글로벌비즈니스학전공"),
  UniversityPostData(topic='ccd', base_url="https://ccd.jnu.ac.kr", bbs_url="https://ccd.jnu.ac.kr/ccd/1865/subview.do", name="문화콘텐츠학부"),
  UniversityPostData(topic='ctm', base_url="https://ctm.jnu.ac.kr", bbs_url="https://ctm.jnu.ac.kr/ctm/13500/subview.do", name="문화관광경영학과"),
  ## 수산해양대학(여수)
  UniversityPostData(topic='engineer', base_url="https://engineer.jnu.ac.kr", bbs_url="https://engineer.jnu.ac.kr/engineer/2842/subview.do", name="기관시스템공학과"),
  UniversityPostData(topic='fishpath', base_url="https://fishpath.jnu.ac.kr", bbs_url="https://fishpath.jnu.ac.kr/fishpath/3509/subview.do", name="수산생명의학과"),
  UniversityPostData(topic='smartfish', base_url="https://smartfish.jnu.ac.kr", bbs_url="https://smartfish.jnu.ac.kr/smartfish/367/subview.do", name="스마트수산자원관리학과"),
  UniversityPostData(topic='aqua', base_url="https://aqua.jnu.ac.kr", bbs_url="https://aqua.jnu.ac.kr/aqua/1009/subview.do", name="양식생물학과"),
  UniversityPostData(topic='oceaneng', base_url="https://oceaneng.jnu.ac.kr", bbs_url="https://oceaneng.jnu.ac.kr/oceaneng/2498/subview.do", name="조선해양공학과"),
  UniversityPostData(topic='police', base_url="https://police.jnu.ac.kr", bbs_url="https://police.jnu.ac.kr/police/2669/subview.do", name="해양경찰학과"),
  UniversityPostData(topic='marinefs', base_url="https://marinefs.jnu.ac.kr", bbs_url="https://marinefs.jnu.ac.kr/marinefs/2894/subview.do", name="해양바이오식품학과"),
  UniversityPostData(topic='marine', base_url="https://marine.jnu.ac.kr", bbs_url="https://marine.jnu.ac.kr/marine/2756/subview.do", name="해양생산관리학과"),
  UniversityPostData(topic='ocean89', base_url="https://ocean89.jnu.ac.kr", bbs_url="https://ocean89.jnu.ac.kr/ocean89/2592/subview.do", name="해양융합과학과"),
  UniversityPostData(topic='dfmitl', base_url="https://dfmitl.jnu.ac.kr", bbs_url="https://dfmitl.jnu.ac.kr/dfmitl/3202/subview.do", name="수산해양산업관광레저융합학과(계약학과)"),
  ## 창의융합학부(여수)
  UniversityPostData(topic='fcc', base_url="https://fcc.jnu.ac.kr", bbs_url="https://fcc.jnu.ac.kr/fcc/18180/subview.do", name="창의융합학부")
]

def departments_crawling():
  print("> 학과 크롤링")
  for department_data in department_data_list:
    general_bbs_crawling(post_data=department_data, post_model=DepartmentPost, set_model=DepartmentSet)