# Login model

# Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


# Utilities abstracto base
from utils import GestioninModel
from users.models import Rol


class User(GestioninModel, AbstractBaseUser):
    USERNAME_FIELD = 'dni'

    dni = models.PositiveIntegerField(
        unique=True
    )

    rol = models.ForeignKey(
        Rol,
        on_delete=models.CASCADE
    )

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.dni
