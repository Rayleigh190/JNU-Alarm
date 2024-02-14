from .collegeCron import *
from .departmentCron import *

def crawling_job():
  department_craling_job()
  college_craling_job()

def department_craling_job():
  architecture_crawling()
  materials_engineering_crawling()
  mechanical_engineering_crawling()
  biotechnology_crawling()
  materials_science_engineering_crawling()
  software_engineering_crawling()

def college_craling_job():
  engineering_crawling()