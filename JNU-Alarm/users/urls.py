from django.urls import path, include
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path("register/", RegisterView.as_view()),
  path("login/", LoginView.as_view()),
  path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]