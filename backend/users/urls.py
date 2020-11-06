from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users.views import (
    # UserLoginAPIView,
    # UserAPIView,
    # RolAPIView,
    # UserSignUpAPIView,
    UserViewSet
)


route = DefaultRouter()
route.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(route.urls)),
    # path('users/', UserAPIView.as_view()),
    # path('users/login/', UserLoginAPIView.as_view()),
    # path('users/signup/', UserSignUpAPIView.as_view()),
    # path('rols/', RolAPIView.as_view())
]
