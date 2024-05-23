from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    driver = models.ForeignKey(User, related_name='driver', on_delete=models.CASCADE)
    passengers = models.ManyToManyField(User, related_name='passengers')
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    departure_time = models.DateTimeField()

    def __str__(self):
        return f"{self.start_location} to {self.end_location} by {self.driver.username}"
