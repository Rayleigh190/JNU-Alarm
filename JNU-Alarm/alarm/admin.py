from django.contrib import admin

# Register your models here.
from .models import Device, DepartmentPost, Notification, Setting, BasicSet, DepartmentSet, CollegeSet, CollegePost, HomePost

admin.site.register([
    Device,
    Notification,
    Setting,
    BasicSet,
])

# 홈페이지
admin.site.register([
    HomePost,
])

# 단과대
admin.site.register([
    CollegeSet,
    CollegePost,
])

# 학과
admin.site.register([
    DepartmentSet,
    DepartmentPost,
])