from rest_framework import status
from rest_framework.response import Response  
from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Device, Setting, Basic, College, Department
from .serializer import DeviceCreateSerializer, BasicSerializer, SettingSerializer, CollegeSerializer, DepartmentSerializer


class DeivceView(APIView):
  """
  * 디바이스 등록
  * 앱 설치후 첫 실행시 요청
  1. 새로운 device_id(유저)일 경우 받은 device_id로 생성한다.
  2. 이미 가입된 Device라면 true 반환한다.
  """
  def post(self, request, *args, **kwargs):
    serializer = DeviceCreateSerializer(data=request.data)
    device_id = serializer.initial_data.get('device_id')

    # If the device already exists, update the fcm_token
    if Device.objects.filter(device_id=device_id).exists():
      result_dic = {'success': True, 'response': None, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)
    
    # If the device does not exist, create a new device
    if serializer.is_valid():
      basic = Basic.objects.create()
      department = Department.objects.create()
      college = College.objects.create()
      setting = Setting.objects.create(basic=basic, college=college, department=department)
      Device.objects.create(device_id=device_id, setting=setting)
      result_dic = {'success': True, 'response': None, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)
    
    result_dic = {'success': False, 'response': None, 'error': None}
    return Response(result_dic, status=status.HTTP_400_BAD_REQUEST)
  
class SettingBasicView(APIView):
  """
  * 디바이스 기본 설정 조회
  * 디바이스 기본 설정 정보를 받아 올 수 있다.
  """
  def get(self, request, *args, **kwargs):
    device_id = request.GET.get('device-id')
    device = get_object_or_404(Device, device_id=device_id)
    basic_serializer = BasicSerializer(device.setting.basic)
    result_dic = {'success': True, 'response': basic_serializer.data, 'error': None}
    return Response(result_dic, status=status.HTTP_200_OK)
    
  """
  * 디바이스 기본 설정 수정
  * 디바이스 기본 설정 정보를 수정할 수 있다.
  """
  def post(self, request, *args, **kwargs):
    device_id = request.GET.get('device-id')
    device = get_object_or_404(Device, device_id=device_id)
    serializer = BasicSerializer(data=request.data)

    if serializer.is_valid():
      # Update data
      device.setting.basic.weather = serializer.validated_data.get('weather')
      device.setting.basic.emergency = serializer.validated_data.get('emergency')
      device.setting.basic.save()
      
      res_serializer = BasicSerializer(device.setting.basic)
    
      result_dic = {'success': True, 'response': res_serializer.data, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)

    result_dic = {'success': False, 'response': None, 'error': serializer.errors}
    return Response(result_dic, status=status.HTTP_400_BAD_REQUEST)
  
class SettingDepartmentView(APIView):
  """
  * 디바이스 학과 설정 조회
  * 디바이스 학과 설정 정보를 받아 올 수 있다.
  """
  def get(self, request, *args, **kwargs):
    device_id = request.GET.get('device-id')
    device = get_object_or_404(Device, device_id=device_id)
    department_serializer = DepartmentSerializer(device.setting.department)
    result_dic = {'success': True, 'response': department_serializer.data, 'error': None}
    return Response(result_dic, status=status.HTTP_200_OK)
    
  """
  * 디바이스 학과 설정 수정
  * 디바이스 학과 설정 정보를 수정할 수 있다.
  """
  def post(self, request, *args, **kwargs):
    device_id = request.GET.get('device-id')
    device = get_object_or_404(Device, device_id=device_id)
    serializer = DepartmentSerializer(data=request.data)

    if serializer.is_valid():
      # Update data
      department_data = serializer.validated_data
      department = device.setting.department
      department.software_engineering = department_data.get('software_engineering')
      department.electric_engineering = department_data.get('electric_engineering')
      department.save()
      res_serializer = DepartmentSerializer(department)
    
      result_dic = {'success': True, 'response': res_serializer.data, 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)

    result_dic = {'success': False, 'response': None, 'error': serializer.errors}
    return Response(result_dic, status=status.HTTP_400_BAD_REQUEST)