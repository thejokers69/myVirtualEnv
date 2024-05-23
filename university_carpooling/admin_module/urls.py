# admin_module/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('carpools/', views.carpool_list, name='carpool_list'),
    path('carpools/<int:pk>/', views.carpool_detail, name='carpool_detail'),
]
