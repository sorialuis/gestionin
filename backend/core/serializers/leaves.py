# Django REST Framework
from rest_framework import serializers

# Models
from core.models import Leave

from users.serializers import UserModelSerializer


class LeaveModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()
    class Mete:
        model = Leave
        fields = {
            'id',
            'user',
            'from_date',
            'note',
            'days'
        }
