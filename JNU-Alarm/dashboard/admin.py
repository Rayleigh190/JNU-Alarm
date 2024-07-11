from django.contrib import admin

# Register your models here.
from .models import Shortcut

class ShortcutAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_webview', 'is_modal',)
  list_display_links = ('name',)

admin.site.register(Shortcut, ShortcutAdmin)