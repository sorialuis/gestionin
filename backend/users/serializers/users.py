# Users serializers

# Django
from django.contrib.auth import authenticate

# Django REST Framekork
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Model
from users.models import User


class UserSerializer(serializers.Serializer):
    dni = serializers.IntegerField()
    password = serializers.CharField()
    rol = serializers.IntegerField()


class CreateUserSerializer(serializers.Serializer):
    dni = serializers.IntegerField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    password = serializers.CharField()
    rol_id = serializers.IntegerField()

    def create(self, data):
        # user = User(**data)
        # test = user.set_password(raw_password=user.password)
        # print(test)
        user = User(**data)
        user.set_password(data['password'])
        return User.objects.create(
            dni=user.dni,
            password=user.password,
            rol=user.rol
        )

class UserModelSerializer(serializers.ModelSerializer):
    rol = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = (
            'dni',
            'rol',
        )


class UserLoginSerializer(serializers.Serializer):
    # Handle the login request data
    dni = serializers.IntegerField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        # Check credentials
        user = authenticate(
            username=data['dni'],
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        # Generate or retrieve new token
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
