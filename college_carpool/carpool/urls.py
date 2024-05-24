# carpool/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_ride, name='create_ride'),
    path('search/', views.search_ride, name='search_ride'),
]