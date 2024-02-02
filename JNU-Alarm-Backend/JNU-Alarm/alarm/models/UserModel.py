from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .SettingModel import Setting
from .BasicModel import Basic
from .CollegeModel import College
from .DepartmentModel import Department

# 사용자 계정 관련
class UserManager(BaseUserManager):
  def create_user(self, device_id, fcm_token, password=None, setting=None, **extra_fields):
    if not setting:
      # Create a default setting if none is provided
      basic = Basic.objects.create()
      college = College.objects.create()
      department = Department.objects.create()
      setting = Setting.objects.create(basic=basic, college=college, department=department)

    user = self.model(device_id=device_id, fcm_token=fcm_token, setting=setting, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, device_id, fcm_token, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    # Create a default setting for the superuser
    basic = Basic.objects.create()
    college = College.objects.create()
    department = Department.objects.create()
    setting = Setting.objects.create(basic=basic, college=college, department=department)

    return self.create_user(device_id, fcm_token, password, setting=setting, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
  device_id = models.TextField(unique=True, blank=False, null=False)
  fcm_token = models.TextField(unique=True)
  setting = models.ForeignKey(Setting, on_delete=models.CASCADE)

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = UserManager()

  REQUIRED_FIELDS = ['fcm_token']  # Add any additional fields required for createsuperuser

  def __str__(self):
      return self.device_id

  @property
  def username(self):
      return self.device_id

  USERNAME_FIELD = 'device_id'