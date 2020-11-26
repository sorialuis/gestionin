# Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import Rol


class RolSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    rol = serializers.CharField()
    auth_lvl = serializers.IntegerField()


class CreateRolSerializer(serializers.Serializer):
    rol = serializers.CharField(
        validators=[
            UniqueValidator(queryset=Rol.objects.all())
        ]
    )
    auth_lvl = serializers.IntegerField()

    def create(self, data):
        return Rol.objects.create(**data)


class RolModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rol
        fields = (
            'id',
            'rol',
            'auth_lvl'
        )
