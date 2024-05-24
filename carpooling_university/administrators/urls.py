from django.urls import path
from . import views

urlpatterns = [
    path('manage_users/', views.manage_users, name='manage_users'),
    path('moderate_content/', views.moderate_content, name='moderate_content'),
    path('generate_reports/', views.generate_reports, name='generate_reports'),
]