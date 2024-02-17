from rest_framework import serializers
from .models import Notification, Question

class NotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    fields = [
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