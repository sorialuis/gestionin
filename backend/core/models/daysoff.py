# Django
from django.db import models


# Utils
from utils import GestioninModel


class DaysOff(GestioninModel):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )
    day = models.DateField(
        primary_key=True
    )
    requested = models.BooleanField(
        default=False
    )
    note = models.CharField(
        max_length=150
    )

    class Meta:
        unique_together = (('user', 'day'),)
