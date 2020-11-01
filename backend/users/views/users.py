# User Views

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# from rest_framework.mixins import

# Models
from users.models import User

# Serializers
from users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    CreateUserSerializer,
    UserSerializer
)


# @api_view()
# def list_users(request):
#     users = User.objects.all()
#     data = []
#     for user in users:
#         data.append({
#             'dni': user.dni,
#             'rol': user.rol,
#         })
#     return Response(data)
#
#
# @api_view(['POST'])
# def create_user(request):
#
#     serializer = CreateUserSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.save()
#     return Response(UserSerializer(user).data)


class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        # data = []
        # for user in users:
        #     data.append({
        #         'dni': user.dni,
        #         # 'rol': user.rol,
        #     })
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # return Response(UserSerializer(user).data)
        # return Response(serializer.data)
        return Response(UserModelSerializer(user).data)


class UserLoginAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        # return Response(data, status=status.HTTP_201_CREATED)
        return Response(data)

