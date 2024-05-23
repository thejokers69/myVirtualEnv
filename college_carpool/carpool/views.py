from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Ride

def index(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'carpool/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'carpool/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'carpool/login.html')

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    rides = Ride.objects.filter(driver=profile) | Ride.objects.filter(passengers=profile)
    return render(request, 'carpool/profile.html', {'profile': profile, 'rides': rides})

@login_required
def create_ride(request):
    if request.method == 'POST':
        start_location = request.POST['start_location']
        end_location = request.POST['end_location']
        departure_time = request.POST['departure_time']
        driver = Profile.objects.get(user=request.user)
        Ride.objects.create(driver=driver, start_location=start_location, end_location=end_location, departure_time=departure_time)
        return redirect('profile')
    return render(request, 'carpool/ride.html')
