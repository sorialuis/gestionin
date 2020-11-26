# Django REST Framework
from rest_framework import serializers

from core.models import DaysOff

from users.serializers import UserModelSerializer


class DaysOffModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = DaysOff
        fields = (
            'id',
            'user',
            'day',
            'requested',
            'note'
        )
