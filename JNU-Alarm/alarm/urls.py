from django.urls import path, include
from .views import NotificationView

urlpatterns = [
  path("notification/", NotificationView.as_view()),
]