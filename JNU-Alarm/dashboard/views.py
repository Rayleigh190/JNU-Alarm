from rest_framework import status
from rest_framework.response import Response  
from rest_framework.views import APIView
from .models import Shortcut
from .serializer import ShortcutSerializer

class ShortcutView(APIView):
  def get(self, request):
    shortcut = Shortcut.objects.all()
    serializer = ShortcutSerializer(shortcut, many=True)
    result_dic = {
      'success': True, 
      'response': serializer.data, 
      'error': None
    }
    return Response(result_dic, status=status.HTTP_200_OK)
