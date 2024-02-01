from rest_framework import serializers
from .models import User, Setting, Basic, College, Department

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    token['user_id'] = user.id
    return token

class UserCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'device_id',
      'fcm_token',
    ]

class BasicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Basic
    exclude = ['id']

class CollegeSerializer(serializers.ModelSerializer):
  class Meta:
    model = College
    exclude = ['id']

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    exclude = ['id']

class SettingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Setting
    fields = '__all__'