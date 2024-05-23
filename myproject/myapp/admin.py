from django.contrib import admin
from .models import Utilisateur, Trajet, Reservation, Localisation

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

class TrajetAdmin(admin.ModelAdmin):
    list_display = ['pointDepart', 'pointArrivee', 'dateDepart', 'heureDepart', 'placesDisponibles', 'prix']
    list_filter = ['dateDepart', 'pointDepart', 'pointArrivee']
    search_fields = ['pointDepart', 'pointArrivee']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['utilisateur', 'trajet', 'statutReservation']
    list_filter = ['statutReservation']
    search_fields = ['utilisateur__username', 'trajet__pointDepart']

class LocalisationAdmin(admin.ModelAdmin):
    list_display = ['latitude', 'longitude']

admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Trajet, TrajetAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Localisation, LocalisationAdmin)
