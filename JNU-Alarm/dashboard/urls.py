from django.urls import path, include
from .views import ShortcutView

urlpatterns = [
  path("shortcut/", ShortcutView.as_view()),
]