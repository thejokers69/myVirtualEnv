# carpool/forms.py
from django import forms
from .models import Ride, Booking

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['departure', 'destination', 'departure_time', 'seats_available']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['ride']
