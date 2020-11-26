# Django REST Framework
from rest_framework import serializers

# Models
from users.models import UserDetails


class UserDetailsModelSerializer(serializers.ModelSerializer):

    team = serializers.StringRelatedField()

    class Meta:
        model = UserDetails
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'team'
        )
