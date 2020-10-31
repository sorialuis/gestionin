from django.urls import path

from users.views import (
    # list_users,
    # create_user,
    create_rol,
    list_rols,
    UserLoginAPIView,
    UserAPIView,
)


urlpatterns = [
    # path('users/', list_users),
    # path('users/create/', create_user),
    path('users/', UserAPIView.as_view()),
    path('users/login/', UserLoginAPIView.as_view()),
    path('users/rol/create/', create_rol),
    path('users/rol/', list_rols),
]
