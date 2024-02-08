from django.contrib import admin

# Register your models here.
from .models import Device, Notification, Setting, Basic, Department, College
# 학과
from .models import Architecture, MaterialsEngineering, MechanicalEngineering, Biotechnology, SoftwareEngineering
# 단과대
from .models import Engineering

admin.site.register([
    Device,
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
    MaterialsEngineering,
    MechanicalEngineering,
    Biotechnology,
    SoftwareEngineering,
])