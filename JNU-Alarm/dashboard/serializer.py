from rest_framework import serializers
from .models import Shortcut, BannerAd, Restaurant

class ShortcutSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shortcut
    exclude = ['id']

class BannerAdSerializer(serializers.ModelSerializer):
  class Meta:
    model = BannerAd
    exclude = ['id']

class RestaurantSerializer(serializers.ModelSerializer):
  class Meta:
    model = Restaurant
    exclude = ['id', 'is_available']