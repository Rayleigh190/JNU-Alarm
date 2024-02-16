from django.urls import path, include
from .views import NotificationView, SendTopicMessage

urlpatterns = [
  path("notification/", NotificationView.as_view()),
  path("send/topic/", SendTopicMessage.as_view()),
]