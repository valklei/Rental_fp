from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer, UserSerializer
from .models import CustomUser
from .utils import set_jwt_cookies


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'


    # def get_object(self):
    #     return self.request.user



# Create your views here.
class LogInAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                data={"message": "Имя пользователя и пароль обязательны"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if user:
            response = Response(
                data={"message": f"Авторизация для пользователя: {user.username} выполнена"},
                status=status.HTTP_200_OK
            )

            set_jwt_cookies(response=response, user=user)

            return response

        else:
            return Response(
                data={"message": "Не верный логин или пароль"},
                status=status.HTTP_401_UNAUTHORIZED
            )


class LogOutAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:

        # user = request.user
        response = Response(
            data={"message": f"Выход выполнен"},
            status=status.HTTP_200_OK
        )

        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response


