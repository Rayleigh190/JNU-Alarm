from rest_framework import status
from rest_framework.response import Response  
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from firebase_admin import messaging
from .models import Notification, Question
from .serializer import NotificationSerializer, SendNotificationSerializer, QuestionSerializer
from .permissions import SendMessage
from .crons.baseCron import send_topic_message


class NotificationView(APIView):
  def post(self, request, *args, **kwargs):
    # POST 요청에서 'topic' 키에 해당하는 값을 가져옴
    topic_list = request.data.get('topic', [])
    # 'topic' 리스트에 해당하는 알림(Notification)을 필터링하여 가져옴
    notifications = Notification.objects.filter(topic__in=topic_list).order_by('-created_at')[:20]
    serializer = NotificationSerializer(notifications, many=True)
    result_dic = {'success': True, 'response': serializer.data, 'error': None}
    return Response(result_dic, status=status.HTTP_200_OK)


class SendTopicMessage(APIView):
  permission_classes = [SendMessage]

  def post(self, request, *args, **kwargs):
    serializer = SendNotificationSerializer(data=request.data)
    if serializer.is_valid():
      send_topic_message(
        title=serializer.validated_data.get('title'),
        body=serializer.validated_data.get('body'),
        link=serializer.validated_data.get('link'),
        topic=serializer.validated_data.get('topic')
      )
      # serializer.save()
      result_dic = {'success': True, 'response': None, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)
    result_dic = {'success': False, 'response': None, 'error': serializer.errors}
    return Response(result_dic, status=status.HTTP_400_BAD_REQUEST)
  

class QuestionView(APIView):
   def post(self, request, *args, **kwargs):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      result_dic = {'success': True, 'response': None, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)
    result_dic = {'success': False, 'response': None, 'error': serializer.errors}
    return Response(result_dic, status=status.HTTP_400_BAD_REQUEST)