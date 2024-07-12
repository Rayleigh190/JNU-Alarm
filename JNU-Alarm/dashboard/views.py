from rest_framework import status
from rest_framework.response import Response  
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from .models import Shortcut, BannerAd
from .serializer import ShortcutSerializer, BannerAdSerializer
from django.utils import timezone
import random

class ShortcutView(APIView):
  @method_decorator(cache_control(max_age=3600))
  def get(self, request):
    shortcut = Shortcut.objects.filter(is_available=True)
    serializer = ShortcutSerializer(shortcut, many=True)
    result_dic = {
      'success': True, 
      'response': serializer.data, 
      'error': None
    }
    return Response(result_dic, status=status.HTTP_200_OK)
  
class BannerAdView(APIView):
  @method_decorator(cache_control(max_age=10))
  def get(self, request):
    today = timezone.now()
    bannerAds = BannerAd.objects.filter(is_available=True, expiry_date__gte=today)
    random_ad = random.choice(bannerAds)
    serializer = BannerAdSerializer(random_ad)
    result_dic = {
      'success': True,
      'response': serializer.data,
      'error': None
    }
    return Response(result_dic, status=status.HTTP_200_OK)
