from django.urls import path, include
from .views import UserView, SettingView

urlpatterns = [
  path("user/", UserView.as_view()),
  path("setting/", SettingView.as_view()),
]