from rest_framework import status
from rest_framework.response import Response  
from rest_framework.views import APIView  
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse

from .models import User, Setting, Department, College
from .serializer import UserCreateSerializer, SettingSerializer, DepartmentSerializer, CollegeSerializer, SettingUpdateSerializer

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)

  return {
    'refresh': str(refresh),
    'access': str(refresh.access_token),
  }

class UserView(APIView):
  """
  * 사용자 등록
  * 앱 설치후 첫 실행시 요청
  1. 새로운 device_id(유저)일 경우 받은 device_id와 fcm_token으로 User를 생성한다.
  2. 이미 가입된 User라면 새로 받은 fcm_token으로 수정한다.
  """
  def post(self, request, *args, **kwargs):
    serializer = UserCreateSerializer(data=request.data)
    device_id = serializer.initial_data.get('device_id')
    fcm_token = serializer.initial_data.get('fcm_token')

    # If the user already exists, update the fcm_token
    if User.objects.filter(device_id=device_id).exists():
      user_obj = User.objects.get(device_id=device_id)
      user_obj.fcm_token = fcm_token
      user_obj.save()
      token = get_tokens_for_user(user_obj)
      response = JsonResponse({
        'success': True, 
        'response': None, 
        'error': None
        }, status=status.HTTP_201_CREATED)
      response['Authorization'] = f'Bearer {token["access"]}'
      response.set_cookie('refresh_token', token['refresh'], httponly=True)
      return response
    
    # If the user does not exist, create a new user
    if serializer.is_valid():
      department = Department.objects.create()
      college = College.objects.create()
      setting = Setting.objects.create(college=college, department=department)
      user = User.objects.create(device_id=device_id, fcm_token=fcm_token, setting=setting)

      token = get_tokens_for_user(user)
      response = JsonResponse({
        'success': True, 
        'response': None, 
        'error': None
        }, status=status.HTTP_201_CREATED)
      response['Authorization'] = f'Bearer {token["access"]}'
      # 쿠미 만료 시간 설정
      response.set_cookie('refresh_token', token['refresh'], httponly=True)
      return response
    
    result_dic = {'success': False, 'response': None, 'error': None}
    return Response(result_dic, status=status.HTTP_400_BAD_REQUEST)
  

class SettingView(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  """
  * 사용자 설정 전체 조회
  * 사용자 설정 정보를 받아 올 수 있다.
  """
  def get(self, request, *args, **kwargs):
    try:
      user = User.objects.get(id=request.user.id)
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
    
  """
  * 사용자 설정 수정
  * 사용자 설정 정보를 수정할 수 있다.
  """
  def post(self, request, *args, **kwargs):
    try:
      user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
      result_dic = {'success': False, 'response': None, 'error': 'User not found'}
      return Response(result_dic, status=status.HTTP_404_NOT_FOUND)

    serializer = SettingUpdateSerializer(data=request.data)
    if serializer.is_valid():
      college_data = serializer.validated_data.get('college')
      department_data = serializer.validated_data.get('department')

      # Update college and department data
      user.setting.college.engineering = college_data.get('engineering', user.setting.college.engineering)
      user.setting.college.natural_science = college_data.get('natural_science', user.setting.college.natural_science)

      user.setting.department.software_engineering = department_data.get('software_engineering', user.setting.department.software_engineering)
      user.setting.department.electric_engineering = department_data.get('electric_engineering', user.setting.department.electric_engineering)

      user.setting.college.save()
      user.setting.department.save()
      
      result_dic = {'success': True, 'response': serializer.data, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)

    result_dic = {'success': False, 'response': None, 'error': serializer.errors}
    return Response(result_dic, status=status.HTTP_400_BAD_REQUEST)