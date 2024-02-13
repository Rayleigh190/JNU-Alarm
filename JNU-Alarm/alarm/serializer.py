from rest_framework import serializers
from .models import Device, Notification, Setting, Basic, College, Department


class DeviceCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Device
    fields = [
      'device_id',
    ]

class NotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    fields = [
      'title',
      'body',
      'link',
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