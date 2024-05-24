from django.contrib import admin
from .models import Trip, Reservation, Rating

admin.site.register(Trip)
admin.site.register(Reservation)
admin.site.register(Rating)