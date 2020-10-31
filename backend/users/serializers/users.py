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
    # rol = serializers.RelatedField(source='id', read_only=True)
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
        return User.objects.create(**data)


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'dni',
        )


class UserLoginSerializer(serializers.Serializer):
    # Handle the login reques data
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
