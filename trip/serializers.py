from rest_framework import serializers
from .models import *
from users.serializers import UserSummerySerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ['exif']
      

class TripSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    images = serializers.PrimaryKeyRelatedField(many=True, queryset = Image.objects.all()) ## Performance bug !!! Shoud be nested or hyperlinkRelated Or slug relate??
    places = serializers.PrimaryKeyRelatedField(many=True, queryset = Place.objects.all())
    
    class Meta:
        model = Trip
        fields = '__all__' 

class TripSummerySerializer(serializers.ModelSerializer): 
    #images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    places = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    image_set = ImageSerializer(many=True,read_only=True)
    auther = UserSummerySerializer()

    class Meta:
        model = Trip
        fields = [
            'id' ,
            'subject',
            'category',
            'description',
            'activities',
            'start_date',
            'end_date',
            'auther',
            'image_set',
            'places',
            ]
        read_only_fields = fields

class PlaceSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = Place
        fields = '__all__'
