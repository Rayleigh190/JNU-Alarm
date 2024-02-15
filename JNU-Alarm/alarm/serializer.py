from rest_framework import serializers
from .models import Device, Notification, BasicSet, CollegeSet, DepartmentSet


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

class BasicSetSerializer(serializers.ModelSerializer):
  class Meta:
    model = BasicSet
    exclude = ['id']

class CollegeSetSerializer(serializers.ModelSerializer):
  class Meta:
    model = CollegeSet
    exclude = ['id']

class DepartmentSetSerializer(serializers.ModelSerializer):
  class Meta:
    model = DepartmentSet
    exclude = ['id']