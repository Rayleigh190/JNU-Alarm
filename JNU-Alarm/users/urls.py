from django.urls import path, include
from .views import RegisterView, LoginView, UserFcmInfoView, DevModeView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path("register/", RegisterView.as_view()),
  path("login/", LoginView.as_view()),
  path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
  path("fcm-info/", UserFcmInfoView.as_view()),
  path("dev-mode/", DevModeView.as_view()),
]