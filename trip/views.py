from django.shortcuts import get_object_or_404
from .serializers import TripSerializer, PlaceSerializer
from .models import Trip, Place
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status,request

class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()