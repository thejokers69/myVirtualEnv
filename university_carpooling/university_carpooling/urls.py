# university_carpooling/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_module/', include('admin_module.urls')),
]
