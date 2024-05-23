# admin_app/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Admin(User):
    pass

class Passenger(User):
    pass

class Driver(User):
    car_details = models.TextField()

# carpool/models.py
from django.db import models
from admin_app.models import Passenger, Driver

class Ride(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    seats_available = models.IntegerField()

class Booking(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
