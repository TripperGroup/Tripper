from django.contrib import admin
from .models import Image, Trip, TripCategory, TripActivities

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('latitud','longitud')


admin.site.register(Image,ImageAdmin)
admin.site.register(Trip)
admin.site.register(TripCategory)
admin.site.register(TripActivities)

