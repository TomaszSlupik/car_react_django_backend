from django.shortcuts import render
from .models import Car
from .serializers import CarSerializer
from rest_framework import viewsets

# Create your views here.
class CarViewSet (viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()