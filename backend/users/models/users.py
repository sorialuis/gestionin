# User model

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
# para validar cotra expreciones regulares
from django.core.validators import RegexValidator

# Utilities abstracto base 
from utils import GestioninModel


class User(GestioninModel, AbstractUser):
    # User model
    # extiende de Django AbstractUser

    legajo = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con este legajo'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="El numero tiene que estar en el formato"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'legajo'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True
    )

    is_verfied = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have verified its email address'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username + self.legajo
