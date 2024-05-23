from django import forms
from .models import Trajet

class TrajetForm(forms.ModelForm):
    class Meta:
        model = Trajet
        fields = ['pointDepart', 'pointArrivee', 'dateDepart', 'heureDepart', 'placesDisponibles', 'prix']
