# Rol Model

# Django
from django.db import models


# Utilities abstracto base
from utils import GestioninModel


class Rol(GestioninModel):
    rol = models.CharField(
        max_length=15,
        unique=True
    )

    auth_lvl = models.PositiveSmallIntegerField(
        default=10
    )

    def __str__(self):
        return self.rol
