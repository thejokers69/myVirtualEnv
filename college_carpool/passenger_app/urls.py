from django.urls import path
from . import views

urlpatterns = [
    path('search_trips/', views.search_trips, name='search_trips'),
    path('book_trip/<int:trip_id>/', views.book_trip, name='book_trip'),
    path('rate_driver/<int:trip_id>/', views.rate_driver, name='rate_driver'),
    path('trip_detail/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('profile/', views.profile, name='profile'),
]
