from rest_framework import status
from rest_framework.response import Response  
from rest_framework.views import APIView  

from .models import User, Setting, Department, College
from .serializer import UserCreateSerializer, SettingSerializer, DepartmentSerializer, CollegeSerializer


class UserView(APIView):
  """
  * 앱 설치후 첫 실행시 요청
  1. 새로운 device_id(유저)일 경우 받은 device_id와 fcm_token으로 User를 생성한다.
  2. 이미 가입된 User라면 새로 받은 fcm_token으로 수정한다.
  """
  def post(self, request, *args, **kwargs):
    serializer = UserCreateSerializer(data=request.data)
    device_id = serializer.initial_data.get('device_id')
    fcm_token = serializer.initial_data.get('fcm_token')

    if User.objects.filter(device_id=device_id).exists():
      # If the user already exists, update the fcm_token
      user_obj = User.objects.get(device_id=device_id)
      user_obj.fcm_token = fcm_token
      user_obj.save()

      user_id = user_obj.id
      result_dic = {'success': True, 'response': {'user_id': user_id}, 'error': None}
      return Response(result_dic, status=status.HTTP_201_CREATED)
  
    if serializer.is_valid():
      # If the user does not exist, create a new user
      department = Department.objects.create()
      college = College.objects.create()
      setting = Setting.objects.create(college=college, department=department)
      user = User.objects.create(device_id=device_id, fcm_token=fcm_token, setting=setting)

      user_id = user.id
      result_dic = {'success': True, 'response': {'user_id': user_id}, 'error': None}
      return Response(result_dic, status=status.HTTP_201_CREATED)
    
    result_dic = {'success': False, 'response': None, 'error': None}
    return Response(result_dic, status=status.HTTP_400_BAD_REQUEST)
  

class SettingView(APIView):
  """
  * 사용자 설정 정보를 받아 올 수 있다.
  """
  def get(self, request, user_id, *args, **kwargs):
    try:
      user = User.objects.get(id=user_id)
      department = user.setting.department
      college = user.setting.college
      department_serializer = DepartmentSerializer(department) 
      college_serializer = CollegeSerializer(college)
      response_dic = {'college': college_serializer.data, 'department': department_serializer.data}
      result_dic = {'success': True, 'response': response_dic, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)
    except User.DoesNotExist:
      result_dic = {'success': False, 'response': None, 'error': 'User not found'}
      return Response(result_dic, status=status.HTTP_404_NOT_FOUND)