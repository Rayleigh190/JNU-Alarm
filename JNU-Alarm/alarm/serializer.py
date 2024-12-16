from rest_framework import serializers
from .models import Notification, Question, Device, AppInfo

class NotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    fields = [
      'id',
      'title',
      'body',
      'link',
      'created_at',
    ]

class SendNotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    fields = [
      'title',
      'body',
      'topic',
      'link',
    ]

class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    exclude = ['id']

class DeviceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Device
    exclude = ['id']

class AppInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = AppInfo
    exclude = ['id']