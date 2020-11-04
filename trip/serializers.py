from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    images = ImageSerializer(many=True, read_only=True)
    places = serializers.PrimaryKeyRelatedField(many=True, queryset = Place.objects.all())
    class Meta:
        model = Trip
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = Place
        fields = '__all__'
