from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateTimeField()
    available_seats = models.IntegerField()

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()