from django.urls import path, include
from .views import ShortcutView, BannerAdView

urlpatterns = [
  path("shortcut/", ShortcutView.as_view()),
  path("banner-ad/", BannerAdView.as_view()),
]