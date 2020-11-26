# Login model

# Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


# Utilities abstracto base
from utils import GestioninModel
from users.models import Rol
# from core.models import Team


class User(GestioninModel, AbstractBaseUser):
    USERNAME_FIELD = 'dni'

    dni = models.PositiveIntegerField(
        unique=True
    )

    rol = models.ForeignKey(
        Rol,
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        # Team,
        'core.Team',
        related_name='team',
        on_delete=models.SET_NULL,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )



    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return str(self.dni)
