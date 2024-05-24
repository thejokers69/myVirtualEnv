from django.shortcuts import render, redirect
from .models import Trip, Reservation
from django.contrib.auth.decorators import login_required

@login_required
def search_trips(request):
    if request.method == "POST":
        departure = request.POST['departure']
        destination = request.POST['destination']
        trips = Trip.objects.filter(departure=departure, destination=destination)
        return render(request, 'passengers/search_results.html', {'trips': trips})
    return render(request, 'passengers/search_trips.html')

@login_required
def book_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    if request.method == "POST":
        reservation = Reservation(user=request.user, trip=trip, status='Booked')
        reservation.save()
        return redirect('reservation_success')
    return render(request, 'passengers/book_trip.html', {'trip': trip})