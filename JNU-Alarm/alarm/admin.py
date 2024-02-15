from django.contrib import admin

# Register your models here.
from .models import Device, DepartmentPost, Notification, Setting, BasicSet, DepartmentSet, CollegeSet
# 학과
# 단과대

admin.site.register([
    Device,
    Notification,
    Setting,
    BasicSet,
])

# 단과대
admin.site.register([
    CollegeSet,
])

# 학과
admin.site.register([
    DepartmentSet,
    DepartmentPost,
])