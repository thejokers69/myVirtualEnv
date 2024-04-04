from django.urls import path
from student.views import std_home_view

urlpatterns = [
    path('', std_home_view, name='student-home'),
]