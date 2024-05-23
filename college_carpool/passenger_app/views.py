from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Trip

@login_required
def search_trips(request):
    trips = Trip.objects.all()
    return render(request, 'passenger_app/search_trips.html', {'trips': trips})

@login_required
def book_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip.passengers.add(request.user)
    return redirect('profile')

@login_required
def rate_driver(request, trip_id):
    return redirect('profile')

@login_required
def profile(request):
    user_trips = Trip.objects.filter(passengers=request.user)
    return render(request, 'passenger_app/profile.html', {'trips': user_trips})
@login_required
def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    return render(request, 'passenger_app/trip_detail.html', {'trip': trip})

@login_required
def rate_driver(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == 'POST':
        rating = request.POST['rating']
        # Assuming you have a Rating model
        Rating.objects.create(trip=trip, user=request.user, rating=rating)
        return redirect('profile')
    return render(request, 'passenger_app/rate_driver.html', {'trip': trip})
