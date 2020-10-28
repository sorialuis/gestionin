# Users app
# Esto convierte a este modulo en una app de django

# Django
from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    # Users app config
    name = 'users'
    verbose_name = 'Users'


