from rest_framework import status
from rest_framework.response import Response  
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from firebase_admin import messaging
from .models import Notification, Question, Device, AppInfo
from .serializer import NotificationSerializer, SendNotificationSerializer, QuestionSerializer, DeviceSerializer, AppInfoSerializer
from .permissions import SendMessage
from .crons.baseCron import send_topic_message
from django.core.exceptions import ObjectDoesNotExist

from .crons.scanCron import send_email


class NotificationView(APIView):
  def post(self, request, *args, **kwargs):
    device_serializer = DeviceSerializer(data=request.data)
    if device_serializer.is_valid():
      topic_list = device_serializer.validated_data.get('subscribed_topics', [])
      device_id = device_serializer.validated_data.get('device_id')
      try:
        device = Device.objects.get(device_id=device_id)
        device.subscribed_topics = topic_list
        device.save()
      except Device.DoesNotExist:
        device_serializer.save()

      # 'topic' 리스트에 해당하는 알림(Notification)을 필터링하여 가져옴
      notifications = Notification.objects.filter(topic__in=topic_list).order_by('-created_at')[:20]
      serializer = NotificationSerializer(notifications, many=True)
      
      result_dic = {'success': True, 'response': serializer.data, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)
    result_dic = {'success': False, 'response': None, 'error': serializer.errors}
    return Response(result_dic, status=status.HTTP_400_BAD_REQUEST)
  def get(self, request, *args, **kwargs):
    topic_list = request.GET.get('topics').split(",")
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
      
      email = serializer.validated_data.get('email')
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content')

      subject = "📢 전대알림에 질문이 등록됐어요"
      content = f'''이메일 : {email}\n
제목 : {title}\n
내용 : {content}
'''
      send_email(subject, content)

      result_dic = {'success': True, 'response': None, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)
    result_dic = {'success': False, 'response': None, 'error': serializer.errors}
    return Response(result_dic, status=status.HTTP_400_BAD_REQUEST)
   

class AppInfoView(APIView):
  def get(self, request):
    try:
      app_infos = AppInfo.objects.last()
      serializer = AppInfoSerializer(app_infos)
      result_dic = {'success': True, 'response': serializer.data, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
      result_dic = {'success': False, 'response': None, 'error': 'AppInfo not found'}
      return Response(result_dic, status=status.HTTP_404_NOT_FOUND)