from .views import CarViewSet
from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register("car", CarViewSet)

urlpatterns = [
    path("serializers", include(router.urls))
]

