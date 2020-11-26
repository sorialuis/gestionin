from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users.views import UserViewSet
from core.views import TeamUserViewSet

route = DefaultRouter()
route.register(r'users', UserViewSet, basename='users')
# route.register(r'users/(?P<dni>[-a-zA-Z0-0_]+)/team',
route.register(r'users/(?P<dni>[^/.]+)/team',
               TeamUserViewSet,
               basename='team'
               )


urlpatterns = [
    path('', include(route.urls))
]
