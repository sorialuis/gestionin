# Django REST Framework
from rest_framework import serializers
from django.utils.text import slugify

from core.models import Team


class TeamModelSerializer(serializers.ModelSerializer):

    leader = serializers.StringRelatedField()

    def create(self, data):
        team = Team(**data)
        team.slug_name = slugify(team.name, allow_unicode=True)
        team = Team.objects.create(
            name=team.name,
            slug_name=team.slug_name
        )
        return team

    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'slug_name',
            'leader'
        )




