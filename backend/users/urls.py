from django.urls import path

from users.views import (
    # list_users,
    # create_user,
    # create_rol,
    # list_rols,
    UserLoginAPIView,
    UserAPIView,
    RolAPIView,
    UserSignUpAPIView
)


urlpatterns = [
    # path('users/', list_users),
    # path('users/create/', create_user),
    # path('users/rol/create/', create_rol),
    # path('users/rol/', list_rols),
    path('users/', UserAPIView.as_view()),
    path('users/login/', UserLoginAPIView.as_view()),
    path('users/signup/', UserSignUpAPIView.as_view()),
    path('rols/', RolAPIView.as_view())
]
