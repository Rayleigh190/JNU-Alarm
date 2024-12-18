import requests
from rest_framework import status, generics
from rest_framework.response import Response  
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings

class RegisterView(APIView):
  def post(self, request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      token = TokenObtainPairSerializer.get_token(user)
      refresh_token = str(token)
      access_token = str(token.access_token)
      res = Response(
          {
            "success": True,
            "response": {
              "token": {
                "access": access_token,
                "refresh": refresh_token,
              },
            },
            "error": None,
          },
          status=status.HTTP_200_OK,
      )
      # res.set_cookie("access", access_token, httponly=True)
      # res.set_cookie("refresh", refresh_token, httponly=True)
      return res
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    token = TokenObtainPairSerializer.get_token(user)
    refresh_token = str(token)
    access_token = str(token.access_token)
    res = Response(
        {
          "success": True,
          "response": {
            "token": {
              "access": access_token,
              "refresh": refresh_token,
            },
          },
          "error": None,
        },
        status=status.HTTP_200_OK,
    )
    return res

class DevModeView(APIView):
  def post(self, request):
    pw = request.data['password']
    if pw == settings.DEV_MODE_PASSWORD:
      return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


import google.auth.transport.requests
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']
# [START retrieve_access_token]
def _get_access_token():
  """Retrieve a valid access token that can be used to authorize requests.

  :return: Access token.
  """
  credentials = service_account.Credentials.from_service_account_file(
    'serviceAccountKey.json', scopes=SCOPES)
  request = google.auth.transport.requests.Request()
  credentials.refresh(request)
  return credentials.token
# [END retrieve_access_token]

class UserFcmInfoView(APIView):
  def get(self, request, *args, **kwargs):
    token = request.query_params.get("token")
    if not token:
      return Response({"error": "Token parameter is required"}, status=400)
    url = f"https://iid.googleapis.com/iid/info/{token}?details=true"
    headers = {
        'Authorization': 'Bearer ' + _get_access_token(),
        'Content-Type': 'application/json; UTF-8',
        'access_token_auth': 'true'
    }
    
    try:
      response = requests.get(url, headers=headers)
      response.raise_for_status()
      result_dic = {'success': True, 'response': response.json(), 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)
    except requests.exceptions.HTTPError as e:
      result_dic = {'success': True, 'response': str(e), 'error': None}
      return Response(result_dic, status=status.HTTP_200_OK)
