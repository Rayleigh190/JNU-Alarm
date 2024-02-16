from django.contrib import admin

# Register your models here.
from .models import Notification, CollegePost, DepartmentPost, HomePost

admin.site.register([
    Notification, # 알림
])

# 게시물
admin.site.register([
    HomePost, # 홈페이지
    CollegePost, # 단과대
    DepartmentPost, # 학과
])