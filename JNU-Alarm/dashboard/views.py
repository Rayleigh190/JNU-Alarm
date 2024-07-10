from rest_framework import status
from rest_framework.response import Response  
from rest_framework.views import APIView
from .models import Shortcuts
from .serializer import ShortcutsSerializer

class ShortcutsView(APIView):
  def get(self, request):
    shortcuts = Shortcuts.objects.all()
    serializer = ShortcutsSerializer(shortcuts, many=True)
    result_dic = {
      'success': True, 
      'response': serializer.data, 
      'error': None
    }
    return Response(result_dic, status=status.HTTP_200_OK)
