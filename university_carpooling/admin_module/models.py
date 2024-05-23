# admin_module/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_carpooler = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add this line
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Carpool(models.Model):
    driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='driven_carpools')
    passengers = models.ManyToManyField(CustomUser, related_name='passenger_carpools')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)
