from rest_framework import serializers
from .models import Shortcut, BannerAd

class ShortcutSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shortcut
    exclude = ['id']

class BannerAdSerializer(serializers.ModelSerializer):
  class Meta:
    model = BannerAd
    exclude = ['id']