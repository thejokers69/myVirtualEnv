from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)

class Report(models.Model):
    generated_at = models.DateTimeField(auto_now_add=True)
    total_trips = models.IntegerField()
    total_users = models.IntegerField()
    average_ratings = models.FloatField()