from .collegeCron import *
from .departmentCron import *
from .homeCron import *
from .businessCron import *
from .otherCron import *
from .otherBusinessCron.semiCron import *

def crawling_job():
  homes_crawling()
  departments_crawling()
  other_crawling()
  colleges_crawling()
  business_crawling()
  semi_business_crawling()

def scan_crawling_job():
  homes_scan()
  departments_scan()
  colleges_scan()