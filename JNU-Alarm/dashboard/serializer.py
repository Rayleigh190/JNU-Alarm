from rest_framework import serializers
from .models import Shortcut

class ShortcutSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shortcut
    exclude = ['id']