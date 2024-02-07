from django.contrib import admin

# Register your models here.
from .models import User, Notification, Setting, Basic, Department, College
# 학과
from .models import Architecture, SoftwareEngineering
# 단과대
from .models import Engineering

admin.site.register([
    User,
    Notification,
    Setting,
    Basic,
])

# 단과대
admin.site.register([
    College,
    Engineering,
])

# 학과
admin.site.register([
    Department,
    Architecture,
    SoftwareEngineering,
])