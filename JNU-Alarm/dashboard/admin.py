from django.contrib import admin

# Register your models here.
from .models import Shortcut, BannerAd, Restaurant

class ShortcutAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_available', 'is_webview', 'is_modal',)
  list_display_links = ('name',)

admin.site.register(Shortcut, ShortcutAdmin)

class BannerAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_available', 'expiry_date')
  list_display_links = ('name',)

admin.site.register(BannerAd, BannerAdmin)

class RestaurantAdmin(admin.ModelAdmin):
  list_display = ('name', 'road_address', 'type', 'is_available',)
  list_display_links = ('name', 'road_address',)

admin.site.register(Restaurant, RestaurantAdmin)