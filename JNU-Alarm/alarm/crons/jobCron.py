from .collegeCron import *
from .departmentCron import *
from .homeCron import *
from .businessCron import *

def crawling_job():
  homes_crawling()
  departments_crawling()
  colleges_crawling()
  business_crawling()

def scan_crawling_job():
  departments_scan()
  colleges_scan()