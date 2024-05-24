from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from passengers.models import Rating, Trip
from .models import UserProfile, Report

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'administrators/manage_users.html', {'users': users})

@user_passes_test(is_admin)
def moderate_content(request):
    ratings = Rating.objects.all()
    return render(request, 'administrators/moderate_content.html', {'ratings': ratings})

@user_passes_test(is_admin)
def generate_reports(request):
    if request.method == 'POST':
        total_trips = Trip.objects.count()
        total_users = User.objects.count()
        average_ratings = Rating.objects.aggregate(models.Avg('rating'))['rating__avg']
        report = Report(total_trips=total_trips, total_users=total_users, average_ratings=average_ratings)
        report.save()
        return redirect('report_success')
    return render(request, 'administrators/generate_reports.html')