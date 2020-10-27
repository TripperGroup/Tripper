from django.db import models
from users.models import User
import datetime
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.fields import ArrayField

class Rivable(models.Model):
    pass

class TripActivities(models.Model):
    TYPE_OF_ACTIVITIES_CHOICES = [ ## To Do.
    ('AD', 'Biking'),
    ('WN', 'Hiking'),
    ('CT', 'Running'),
    ## ...
    ]
    title = models.CharField(choices=TYPE_OF_ACTIVITIES_CHOICES, max_length=2, blank=True)

class TripCategory(models.Model):
    TYPE_OF_TRIP_CHOICES = [
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
    title  = models.CharField(choices=TYPE_OF_TRIP_CHOICES, max_length=2)


class Trip(Rivable):
    subject = models.CharField(max_length=200)
    category = models.ManyToManyField(TripCategory)
    activities = models.ManyToManyField(TripActivities)
    created_at = datetime.datetime.now()
    start_date = models.DateField()
    end_date = models.DateField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    geo_json = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['geojson','gpx'])
    ])


class Places(Rivable):
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
    description = models.CharField(max_length=500)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    latitude  = models.DecimalField(max_digits=9, decimal_places=6, null=True)    
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.CharField(max_length=50)


class Companions(models.Model):
    trip = models.ForeignKey(Trip,on_delete=models.DO_NOTHING)    
    companion = models.ForeignKey(User,on_delete=models.DO_NOTHING)


class Images(models.Model):
    image_id = models.ForeignKey(Rivable, related_name='images', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/Places')
    default_image = models.BooleanField(default=False)
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    


class Accomodation(Rivable):
    api_id = models.CharField(max_length=100)
    pass

class Reviews(models.Model):
    rivable = models.ForeignKey(Rivable, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    created_at = datetime.datetime.now()
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    helpful = models.PositiveIntegerField()

class Transfer(models.Model):
    api_id = models.CharField(max_length=100)
    pass

class TripAccomodation(models.Model):
    pass
class TripPlaces(models.Model):
    pass
class TripTrasnsfers(models.Model):
    pass
