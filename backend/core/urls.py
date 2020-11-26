from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.views import TeamViewSet

route = DefaultRouter()
route.register(r'teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('', include(route.urls))
]
