# Francos model

# Django
from django.db import models

from utils import GestioninModel
from users.models import User


class Franco(GestioninModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    dia = models.DateField(
        primary_key=True
    )

    class Meta:
        unique_together = (('user', 'dia'),)
