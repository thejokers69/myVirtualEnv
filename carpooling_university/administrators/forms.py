from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['total_trips', 'total_users', 'average_ratings']