# Django models utilites 

# Django
from django.db import models


class GestioninModel(models.Model):
    # Modelo base para todo el proyecto (abstracto)

    created = models.DateTimeField(
        'created at',
        # Se graba la fecha de forma automatica
        auto_now_add=True,
        help_text='Cuando el objeto fue creado'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Cuando fue modificado por ultima vez'
    )

    class Meta:
        # Meta options
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
