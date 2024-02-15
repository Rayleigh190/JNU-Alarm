from .baseCron import general_bbs_crawling, UniversityPostData
from ..models import CollegePost, CollegeSet

college_data_list = [
  UniversityPostData(topic='cba', base_url="https://cba.jnu.ac.kr", bbs_url="https://cba.jnu.ac.kr/cba/13919/subview.do", name="경영대학"),
  UniversityPostData(topic='eng', base_url="https://eng.jnu.ac.kr", bbs_url="https://eng.jnu.ac.kr/eng/7343/subview.do", name="공과대학"),
  UniversityPostData(topic='agric', base_url="https://agric.jnu.ac.kr", bbs_url="https://agric.jnu.ac.kr/agric/4638/subview.do", name="농업생명과학대학"),
  UniversityPostData(topic='education', base_url="https://education.jnu.ac.kr", bbs_url="https://education.jnu.ac.kr/education/15284/subview.do", name="사범대학"),
  UniversityPostData(topic='socsci', base_url="https://socsci.jnu.ac.kr", bbs_url="https://socsci.jnu.ac.kr/socsci/8806/subview.do", name="사회과학대학"),
  UniversityPostData(topic='humanecology', base_url="https://humanecology.jnu.ac.kr", bbs_url="https://humanecology.jnu.ac.kr/humanecology/12765/subview.do", name="생활과학대학"),
  UniversityPostData(topic='vetmed', base_url="https://vetmed.jnu.ac.kr", bbs_url="https://vetmed.jnu.ac.kr/vetmed/12818/subview.do", name="수의과대학"),
  UniversityPostData(topic='pharmacy', base_url="https://pharmacy.jnu.ac.kr", bbs_url="https://pharmacy.jnu.ac.kr/pharmacy/7190/subview.do", name="약학대학"),
  UniversityPostData(topic='arts', base_url="https://arts.jnu.ac.kr", bbs_url="https://arts.jnu.ac.kr/arts/12862/subview.do", name="예술대학"),
  # UniversityPostData(topic='', base_url="", bbs_url="", name="의과대학"),
  UniversityPostData(topic='human', base_url="https://human.jnu.ac.kr", bbs_url="https://human.jnu.ac.kr/human/15014/subview.do", name="인문대학"),
  UniversityPostData(topic='natural', base_url="https://natural.jnu.ac.kr", bbs_url="https://natural.jnu.ac.kr/natural/14487/subview.do", name="자연과학대학"),
  UniversityPostData(topic='cvg', base_url="https://cvg.jnu.ac.kr", bbs_url="https://cvg.jnu.ac.kr/cvg/3608/subview.do", name="AI융합대학"),
  UniversityPostData(topic='engc', base_url="https://engc.jnu.ac.kr", bbs_url="https://engc.jnu.ac.kr/engc/2167/subview.do", name="공학대학"),
  UniversityPostData(topic='yculture', base_url="https://yculture.jnu.ac.kr", bbs_url="https://yculture.jnu.ac.kr/yculture/17318/subview.do", name="문화사회과학대학"),
  UniversityPostData(topic='sea', base_url="https://sea.jnu.ac.kr", bbs_url="https://sea.jnu.ac.kr/sea/3465/subview.do", name="수산해양대학"),
]

def colleges_crawling():
  print("> 단과대 크롤링")
  for college_data in college_data_list:
    general_bbs_crawling(post_data=college_data, post_model=CollegePost, set_model=CollegeSet)