# Django REST Framework
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

# Models
from core.models import Team
from users.models import User

# Serializers
from core.serializers import TeamModelSerializer
from users.serializers import UserModelSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from users.permissions import IsSupervisor
from users.permissions import IsAccountOwner
from core.permissions import IsInclude


class TeamViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Team.objects.all()
    serializer_class = TeamModelSerializer
    lookup_field = 'slug_name'

    def get_permissions(self):
        if self.action in ['list', 'update', 'partial_update', 'created']:
            permissions = [IsAuthenticated, (IsAdmin | IsSupervisor)]
        elif self.action in ['retrieve']:
            permissions = [IsAuthenticated, (IsAdmin | IsSupervisor | IsInclude)]
        elif self.action in ['destroy']:
            permissions = [IsAuthenticated, IsAdmin]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TeamModelSerializer(instance)
        users = User.objects.all().filter(team=serializer.data['id'])
        serializer_user = UserModelSerializer(users, many=True)
        data = serializer.data
        data['users'] = serializer_user.data
        return Response(data, status=status.HTTP_200_OK)


class TeamUserViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin
):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'dni'

    def get_permissions(self):
        if self.action in ['list']:
            permissions = [IsAuthenticated, (IsAdmin | IsSupervisor | IsAccountOwner)]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        team = instance.team
        serializer_team = TeamModelSerializer(team)
        users = User.objects.all().filter(team=team)
        serializer_user = UserModelSerializer(users, many=True)
        data = serializer_team.data
        data['users'] = serializer_user.data
        return Response(data, status=status.HTTP_200_OK)
