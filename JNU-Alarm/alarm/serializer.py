from rest_framework import serializers
from .models import Device, Setting, Basic, College, Department


class DeviceCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Device
    fields = [
      'device_id',
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