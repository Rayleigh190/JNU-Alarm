from django.urls import path, include
from .views import ShortcutView, BannerAdView, TopBannerAdView, RestaurantRecommendationView

urlpatterns = [
  path("shortcut/", ShortcutView.as_view()),
  path("banner-ad/", BannerAdView.as_view()),
  path("top-banner-ad/", TopBannerAdView.as_view()),
  path("restaurant-recommendation", RestaurantRecommendationView.as_view()),
]