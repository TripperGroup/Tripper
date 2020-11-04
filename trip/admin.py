from django.contrib import admin
from .models import Image, Trip, TripCategory, TripActivities, Review, TripPlaces, UserLinked, Companions, Place


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('latitud','longitud')
    list_display = ('id','subject', 'image') # To show as readable list 

admin.site.register(Review)

admin.site.register(Trip)
admin.site.register(TripCategory)
admin.site.register(TripActivities)
admin.site.register(TripPlaces)
admin.site.register(Image,ImageAdmin)
admin.site.register(UserLinked)
admin.site.register(Companions)
admin.site.register(Place)




