from django.urls import path, include
from .views import NotificationView, SendTopicMessage, QuestionView, AppInfoView

urlpatterns = [
  path("notification/", NotificationView.as_view()),
  path("send/topic/", SendTopicMessage.as_view()),
  path("question/", QuestionView.as_view()),
  path("app-info/", AppInfoView.as_view()),
]