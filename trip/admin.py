from django.contrib import admin
from .models import TripImage, Trip, TripCategory, TripActivities, TripReview, TripPlaces, Companions, Place


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('latitud','longitud')
    list_display = ('id','subject', 'image') # To show as readable list 

admin.site.register(TripReview)

admin.site.register(Trip)
admin.site.register(TripCategory)
admin.site.register(TripActivities)
admin.site.register(TripPlaces)
admin.site.register(TripImage,ImageAdmin)
admin.site.register(Companions)
admin.site.register(Place)




