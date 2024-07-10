from rest_framework import serializers
from .models import Shortcuts

class ShortcutsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Shortcuts
    exclude = ['id']