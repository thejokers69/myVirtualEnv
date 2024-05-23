from django.db import models
from django.contrib.auth.models import AbstractUser

# Extend the default User model
class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=15, blank=True, null=True)
    
    class Meta:
        app_label='myapp'

class Localisation(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class Trajet(models.Model):
    pointDepart = models.CharField(max_length=255)
    pointArrivee = models.CharField(max_length=255)
    dateDepart = models.DateField()
    heureDepart = models.TimeField()
    placesDisponibles = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    localisation = models.ForeignKey(Localisation, on_delete=models.CASCADE, related_name='trajets')

class Reservation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='reservations')
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE, related_name='reservations')
    statutReservation = models.CharField(max_length=50)
