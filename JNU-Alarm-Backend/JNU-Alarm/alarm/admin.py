from django.contrib import admin

# Register your models here.
from .models import User, Setting, Department

admin.site.register(User)
admin.site.register(Setting)
admin.site.register(Department)