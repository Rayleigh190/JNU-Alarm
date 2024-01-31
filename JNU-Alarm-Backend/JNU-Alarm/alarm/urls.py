from django.urls import path, include
from .views import UserRegisterView

urlpatterns = [
  path("user/", UserRegisterView.as_view()),
]