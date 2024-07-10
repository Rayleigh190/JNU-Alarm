from django.urls import path, include
from .views import ShortcutsView

urlpatterns = [
  path("shortcuts/", ShortcutsView.as_view()),
]