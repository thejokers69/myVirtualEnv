from django.shortcuts import render, get_object_or_404, redirect
from .models import Utilisateur, Trajet, Reservation
from django.contrib.auth.decorators import login_required
from .forms import TrajetForm, ReservationForm

@login_required
def list_users(request):
    users = Utilisateur.objects.all()
    return render(request, 'admin/list_users.html', {'users': users})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(Utilisateur, pk=user_id)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserCreationForm(instance=user)
    return render(request, 'admin/edit_user.html', {'form': form})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(Utilisateur, pk=user_id)
    user.delete()
    return redirect('list_users')

@login_required
def manage_trips(request):
    trips = Trajet.objects.all()
    return render(request, 'admin/manage_trips.html', {'trips': trips})

@login_required
def manage_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'admin/manage_reservations.html', {'reservations': reservations})

def my_view(request):
    return render(request, 'myapp/list_users.html')

@login_required
def manage_trips(request):
    # Your view logic here
    return render(request, 'your_app_name/manage_trips.html')


class ManageTripsView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        # Your view logic here
        return render(request, 'your_app_name/manage_trips.html')
# You would need to create HTML templates to match these views.
