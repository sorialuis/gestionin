# User Views

# Django REST Framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from users.permissions import IsAccountOwner

# Models
from users.models import User

# Serializers
from users.serializers import UserModelSerializer
from users.serializers import UserLoginSerializer
from users.serializers import UserSignUpSerializer
from users.serializers import UserDetailsModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'dni'

    def get_permissions(self):
        permissions = False
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', 'profile']:
            permissions = [IsAuthenticated]
            if not IsAdmin:
                permissions.append(IsAccountOwner)
        # else:
        #     permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        user = self.get_object()
        user_detail = user.detail
        partial = request.method == 'PATCH'
        serializer = UserDetailsModelSerializer(
            user_detail,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)
