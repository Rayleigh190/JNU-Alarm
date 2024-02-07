from django.contrib import admin

# Register your models here.
from .models import User, Notification, Setting, Basic, Department, College
from .models import SoftwareEngineering
from .models import Engineering

admin.site.register(User)
admin.site.register(Notification)
admin.site.register(Setting)
admin.site.register(Basic)
admin.site.register(College)
admin.site.register(Engineering)
admin.site.register(Department)
admin.site.register(SoftwareEngineering)