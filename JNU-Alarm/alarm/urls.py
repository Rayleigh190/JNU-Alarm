from django.urls import path, include
from .views import DeivceView, NotificationView, SettingBasicView, DepartmentSetView

urlpatterns = [
  path("device/", DeivceView.as_view()),
  path("notification/", NotificationView.as_view()),
  path("setting/basic/", SettingBasicView.as_view()),
  path("setting/department/", DepartmentSetView.as_view()),
]