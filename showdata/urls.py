from django.urls import path, include
from rest_framework import routers
from .views import ShowDataViewSet

router = routers.DefaultRouter()
router.register(f'data', ShowDataViewSet, basename="data")

urlpatterns = [
    path('', include(router.urls))
]