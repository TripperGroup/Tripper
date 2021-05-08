from django.shortcuts import get_object_or_404
from .serializers import TripSerializer, PlaceSerializer, ImageSerializer, TripSummerySerializer
from .models import Trip, Place, TripImage
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status,request

class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

class TripSummeryViewSet(viewsets.ModelViewSet):
    serializer_class = TripSummerySerializer
    queryset = Trip.objects.all().order_by('-created_at')
    ordering = ['create_date']

class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = TripImage.objects.all()