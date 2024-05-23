from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    is_driver = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Ride(models.Model):
    driver = models.ForeignKey(Profile, related_name='driver', on_delete=models.CASCADE)
    passengers = models.ManyToManyField(Profile, related_name='passengers')
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    departure_time = models.DateTimeField()

    def __str__(self):
        return f"{self.start_location} to {self.end_location} by {self.driver.user.username}"
