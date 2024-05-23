# carpool/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Ride, Booking

def index(request):
    rides = Ride.objects.all()
    return render(request, 'carpool/index.html', {'rides': rides})

def create_ride(request):
    if request.method == 'POST':
        # Logique pour créer un nouveau trajet
        pass
    return render(request, 'carpool/create_ride.html')

def search_ride(request):
    if request.method == 'GET':
        # Logique pour rechercher un trajet
        pass
    return render(request, 'carpool/search_ride.html')
