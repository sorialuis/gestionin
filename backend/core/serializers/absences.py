# Django
from rest_framework import serializers

# Utils
from core.models import Absence



class AbsenceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Absence
        fields = (
            'id',
            'user',
            'day',
            'note',
        )