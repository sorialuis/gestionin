# Detalle_Usuario model

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Validate regular expression
from django.core.validators import RegexValidator

from utils import GestioninModel
from users.models import User
from core.models import Team


class UserDetails(GestioninModel):
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='detail'
    )

    team = models.ForeignKey(
        Team,
        related_name='team',
        on_delete=models.SET_NULL,
        null=True
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="El numero tiene que estar en el formato"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    address = models.CharField(_('address'), max_length=150, blank=True)
