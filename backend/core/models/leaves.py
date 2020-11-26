# Django
from django.db import models

# Utils
from utils import GestioninModel


class Leave(GestioninModel):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )
    from_date = models.DateField(
        primary_key=True
    )
    note = models.CharField(
        max_length=150
    )
    days = models.PositiveIntegerField()

    class Meta:
        unique_together = (('user', 'from_date'),)

