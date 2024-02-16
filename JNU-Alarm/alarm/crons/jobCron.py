from .collegeCron import *
from .departmentCron import *
from .homeCron import *

def crawling_job():
  homes_crawling()
  departments_crawling()
  colleges_crawling()