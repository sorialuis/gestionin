# Django REST Framework
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets

# Models
from core.models import DaysOff
# from users.models import User

# Serializers
from core.serializers import DaysOffModelSerializer


class DaysOffViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin
):
    queryset = DaysOff.objects.all()
    serializer_class = DaysOffModelSerializer
