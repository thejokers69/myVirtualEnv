from django.shortcuts import render
from .models import CustomUser

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_detail(request, id):
    user = CustomUser.objects.get(id=id)
    return render(request, 'users/user_detail.html', {'user': user})
