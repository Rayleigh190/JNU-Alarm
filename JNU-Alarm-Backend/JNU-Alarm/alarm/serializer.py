from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'device_id',
      'fcm_token',
    ]