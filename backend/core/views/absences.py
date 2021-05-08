# Django REST Framework
from rest_framework import viewsets
from rest_framework import mixins

# Models
from core.models import Absence

# Serializers
from core.serializers import AbsenceModelSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from users.permissions import IsSupervisor
from users.permissions import IsAccountOwner
from core.permissions import IsInclude


class AbsenceUserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    queryset = Absence.objects.all()
    serializer_class = AbsenceModelSerializer
    lookup_field = 'dni'

    def get_permissions(self):
        if self.action in ['list']:
            permissions = [IsAuthenticated, (IsAdmin | IsSupervisor | IsAccountOwner)]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]


    #
    # def list(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     absence = instance.absence
    #     serializer_absence = AbsenceModelSerializer(absence)
