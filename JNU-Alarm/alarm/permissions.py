from rest_framework import permissions

class SendMessage(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.user.has_perm('alarm.add_notification') 