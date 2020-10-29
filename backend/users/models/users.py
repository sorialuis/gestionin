# Login model

# Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Utilities abstracto base
from utils import GestioninModel
from users.models import Rol


class User(GestioninModel, AbstractBaseUser):

    dni = models.PositiveIntegerField(
        unique=True
    )

    USERNAME_FIELD = 'dni'

    rol = models.ForeignKey(
        Rol,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.dni
