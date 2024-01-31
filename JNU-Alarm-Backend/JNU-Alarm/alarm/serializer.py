from rest_framework import serializers
from .models import User, Setting, College, Department


class UserCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'device_id',
      'fcm_token',
    ]

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = '__all__'

class CollegeSerializer(serializers.ModelSerializer):
  class Meta:
    model = College
    fields = '__all__'  

class SettingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Setting
    fields = '__all__'