from django.urls import path, include
from .views import UserView, SettingBasicView, SettingDepartmentView

urlpatterns = [
  path("user/", UserView.as_view()),
  path("setting/basic/", SettingBasicView.as_view()),
  path("setting/department/", SettingDepartmentView.as_view()),
]