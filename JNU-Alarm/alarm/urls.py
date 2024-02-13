from django.urls import path, include
from .views import DeivceView, NotificationView, SettingBasicView, SettingDepartmentView

urlpatterns = [
  path("device/", DeivceView.as_view()),
  path("notification/", NotificationView.as_view()),
  path("setting/basic/", SettingBasicView.as_view()),
  path("setting/department/", SettingDepartmentView.as_view()),
]