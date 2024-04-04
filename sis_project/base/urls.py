from django.urls import path
from base.views import base_home_view

urlpatterns = [
    path('', base_home_view, name='base-home'),
]