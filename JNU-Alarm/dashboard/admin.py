from django.contrib import admin

# Register your models here.
from .models import Shortcut, BannerAd, Restaurant

def make_available_action(modeladmin, request, queryset):
    queryset.update(is_available=True)
make_available_action.short_description = "선택된 아이템의 is_available을 True로 변경합니다."

def make_unavailable_action(modeladmin, request, queryset):
    queryset.update(is_available=False)
make_unavailable_action.short_description = "선택된 아이템의 is_available을 False로 변경합니다."

@admin.register(Shortcut)
class ShortcutAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_available', 'is_webview', 'is_modal',)
  actions = [make_available_action, make_unavailable_action]

@admin.register(BannerAd)
class BannerAdmin(admin.ModelAdmin):
  list_display = ('name', 'is_available', 'expiry_date')
  actions = [make_available_action, make_unavailable_action]

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
  list_display = ('name', 'road_address', 'type', 'is_available',)
  list_display_links = ('name', 'road_address',)
  actions = [make_available_action, make_unavailable_action]