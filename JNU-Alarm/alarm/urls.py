from django.urls import path, include
from .views import NotificationView, SendTopicMessage, QuestionView

urlpatterns = [
  path("notification/", NotificationView.as_view()),
  path("send/topic/", SendTopicMessage.as_view()),
  path("question/", QuestionView.as_view()),
]