from django.db import models
from users.models import User
import datetime
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.fields import ArrayField
from exiffield.fields import ExifField
from exiffield.getters import exifgetter
from django.core.validators import MaxValueValidator, MinValueValidator



class Rivable(models.Model):
    pass

class TripActivities(models.Model):
    TYPE_OF_ACTIVITIES_CHOICES = [ ## To Complete. Delete this multi choice 
    ('AD', 'Biking'),
    ('WN', 'Hiking'),
    ('CT', 'Running'),
    ## ...
    ]
    title = models.CharField(choices=TYPE_OF_ACTIVITIES_CHOICES, max_length=2, null=True)

class TripCategory(models.Model):
    TYPE_OF_TRIP_CHOICES = [ # Delete this multi choice
    ('AD', 'Adventure'),
    ('WN', 'Wildlife & Nature'),
    ('CT', 'Cities'),
    ('RU', 'Ruins & temples'),
    ('RT', 'Road trips'),
    ('HK', 'Hiking'),
    ('FD', 'Food & drink'),
    ('AC', 'Art & culture'),
    ('CI', 'Coasts & islans'),
    ('FA', 'Family'),
    ]
    title  = models.CharField(choices=TYPE_OF_TRIP_CHOICES, max_length=2, default=None, null=True)


class Trip(Rivable):
    subject = models.CharField(max_length=200)
    category = models.ManyToManyField(TripCategory, blank=True)
    activities = models.ManyToManyField(TripActivities, blank=True)
    created_at = models.DateField(auto_now=True, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    geo_json = models.FileField(blank=True,null=True,validators=[
        FileExtensionValidator(allowed_extensions=['geojson','gpx'])
    ])

class Place(Rivable):
    TYPE_OF_PLACES_CHOICES = [
    ('WN', 'Wildlife & Nature'),
    ('CT', 'City'),
    ('RU', 'Ruin & temple'),
    ('RD', 'Road'),
    ('MN', 'Mountain'),
    ('RC', 'Restaurent & Coffee'),
    ('MS', 'Museume'),
    ('CI', 'Coast & islan'),
    ('PT', 'Patrol'),
    ('AP', 'Airport'),
    ('BS', 'Bus station'),
    ('HT', 'Hotel'),
    ('PR', 'Park')
    ]
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    latitude  = models.DecimalField(max_digits=9, decimal_places=6, null=True)    
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.CharField(max_length=50,blank=True, null=True)


class Companions(models.Model):
    trip = models.ForeignKey(Trip,on_delete=models.DO_NOTHING)    
    companion = models.ForeignKey(User,on_delete=models.DO_NOTHING)


class Image(models.Model):
    rivable = models.ForeignKey(Rivable, related_name='images', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/Places')
    default_image = models.BooleanField(default=False)
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    latitud = models.CharField(max_length=20, editable = False, null=True)
    longitud = models.CharField(max_length=20, editable = False, null= True)
    exif = ExifField(
        source='image',
        denormalized_fields={
            'latitud': exifgetter('GPSLatitude'),
            'longitud': exifgetter('GPSLongitude'),
        },
    )
    

class Review(models.Model):
    rivable = models.ForeignKey(Rivable, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now=True, blank=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(blank=True, null=True,validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    helpfull = models.IntegerField(default=0,validators=[
            MinValueValidator(0)
        ])

class Transfer(models.Model):
    #api_id = models.CharField(max_length=100)
    pass
class Accomodation(Rivable):
    #api_id = models.CharField(max_length=100)
    pass
class TripAccomodation(models.Model):
    pass
class TripPlaces(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.DO_NOTHING,null=True)
    places = models.ForeignKey(Place, on_delete=models.DO_NOTHING, null=True)
class TripTrasnsfers(models.Model):
    pass


class UserLinked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_trips = models.ManyToManyField(Trip, blank=True,related_name="savedtrips") 
    liked_trips = models.ManyToManyField(Trip, blank=True,related_name="likedtrips") 
    saved_places = models.ManyToManyField(Place, blank=True,related_name="savedplaces") 