from django.contrib import admin

# Register your models here.
from .models import Notification, CollegePost, DepartmentPost, HomePost, BusinessPost, Question, Device

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'topic', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'body', 'topic',)
    readonly_fields=('created_at',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'is_completed', 'created_at')
    list_filter = ('created_at',)
    readonly_fields=('created_at',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'topic',)
    readonly_fields=('created_at',)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'subscribed_topics', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('subscribed_topics',)
    readonly_fields=('created_at', 'updated_at',)

admin.site.register([
    Notification, # 알림
], NotificationAdmin)

admin.site.register([
    Question, # 문의 및 제안
], QuestionAdmin)

# 게시물
admin.site.register([
    HomePost, # 홈페이지
    CollegePost, # 단과대
    DepartmentPost, # 학과
    BusinessPost, # 사업단
], PostAdmin)

admin.site.register(Device, DeviceAdmin)