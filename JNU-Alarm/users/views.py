from rest_framework import status, generics
from rest_framework.response import Response  
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
