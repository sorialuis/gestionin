from django.urls import path

from users.views import list_users
from users.views import create_rol
from users.views import list_rols

urlpatterns = [
    path('users/', list_users),
    path('users/rol/create/', create_rol),
    path('users/rol/', list_rols),
]