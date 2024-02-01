from django.contrib import admin

# Register your models here.
from .models import User, Setting, Basic, Department, College

admin.site.register(User)
admin.site.register(Setting)
admin.site.register(Basic)
admin.site.register(College)
admin.site.register(Department)