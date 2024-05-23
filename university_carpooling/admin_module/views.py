# admin_module/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Carpool
from .forms import CustomUserForm, CarpoolForm

@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'admin_module/user_list.html', {'users': users})

@login_required
def user_detail(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, 'admin_module/user_detail.html', {'user': user})

@login_required
def carpool_list(request):
    carpools = Carpool.objects.all()
    return render(request, 'admin_module/carpool_list.html', {'carpools': carpools})

@login_required
def carpool_detail(request, pk):
    carpool = get_object_or_404(Carpool, pk=pk)
    return render(request, 'admin_module/carpool_detail.html', {'carpool': carpool})
