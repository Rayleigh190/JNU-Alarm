from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    fields = [
      'title',
      'body',
      'link',
      'created_at',
    ]