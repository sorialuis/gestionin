# Team Model

# Django
from django.db import models

# Utilities
from utils import GestioninModel
# from users.models import User


class Team(GestioninModel):
    name = models.CharField(
        max_length=30,
        unique=True
    )

    slug_name = models.CharField(
        max_length=30,
        unique=True,
        default='null'
    )

    leader = models.ForeignKey(
        # User,
        'users.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='leader'
    )

    def __str__(self):
        return self.name
