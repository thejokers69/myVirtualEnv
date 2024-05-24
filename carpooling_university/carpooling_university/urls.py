from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrators/', include('administrators.urls')),
    path('passengers/', include('passengers.urls')),
    path('drivers/', include('drivers.urls')),
]