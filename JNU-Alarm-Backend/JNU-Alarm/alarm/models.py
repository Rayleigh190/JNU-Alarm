from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Department(models.Model):
  software_engineering = models.BooleanField(default=False)
  electric_engineering = models.BooleanField(default=False)

class College(models.Model):
  engineering = models.BooleanField(default=False)
  natural_science = models.BooleanField(default=False)

class Setting(models.Model):
  college = models.ForeignKey(College, on_delete=models.CASCADE)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)

# 사용자 계정 관련
class UserManager(BaseUserManager):
  def create_user(self, device_id, fcm_token, password=None, setting=None, **extra_fields):
    if not setting:
      # Create a default setting if none is provided
      college = College.objects.create()
      department = Department.objects.create()
      setting = Setting.objects.create(college=college, department=department)

    user = self.model(device_id=device_id, fcm_token=fcm_token, setting=setting, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, device_id, fcm_token, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    # Create a default setting for the superuser
    college = College.objects.create()
    department = Department.objects.create()
    setting = Setting.objects.create(college=college, department=department)

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

  # @property
  # def email(self):
  #     return self.fcm_token

  USERNAME_FIELD = 'device_id'


# class User(models.Model):
#   device_id = models.TextField(unique=True, blank=False, null=False)
#   fcm_token = models.TextField(unique=True)
#   setting = models.ForeignKey(Setting, on_delete=models.CASCADE)

#   def __str__(self):
#     return self.device_id