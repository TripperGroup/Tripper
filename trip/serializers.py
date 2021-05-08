from rest_framework import serializers
from .models import *
from users.serializers import UserSummerySerializer
from datetime import date


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripImage
        exclude = ['exif']
      

class TripSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    images = serializers.PrimaryKeyRelatedField(many=True, queryset = TripImage.objects.all()) ## Performance bug !!! Shoud be nested or hyperlinkRelated Or slug relate??
    places = serializers.PrimaryKeyRelatedField(many=True, queryset = Place.objects.all())
    
    class Meta:
        model = Trip
        fields = '__all__' 

class TripSummerySerializer(serializers.ModelSerializer): 
    #images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    places = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    image_set = ImageSerializer(many=True,read_only=True)
    auther = UserSummerySerializer()
    trip_days = serializers.SerializerMethodField('get_days')

    class Meta:
        model = Trip
        fields = [
            'id' ,
            'subject',
            'category',
            'description',
            'activities',
            'auther',
            'image_set',
            'places',
            'trip_days',
            ]
        read_only_fields = fields

    @staticmethod
    def get_days(obj):
        if obj.end_date and obj.start_date : 
            delta = obj.end_date - obj.start_date
            return  delta.days
        else :
            return None

class PlaceSerializer(serializers.ModelSerializer): # pylint: disable=function-redefined
    class Meta:
        model = Place
        fields = '__all__'
