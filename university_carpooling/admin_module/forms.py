# admin_module/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Carpool

class CustomUserForm(UserCreationForm):
    class Meta:
        model: CustomUser
        fields: ['username', 'email', 'is_admin', 'is_carpooler']

class CarpoolForm(forms.ModelForm):
    class Meta:
        model: Carpool
        fields: ['driver', 'passengers', 'start_time', 'end_time', 'start_location', 'end_location', 'approved']
