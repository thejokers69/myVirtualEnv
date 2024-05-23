from django.urls import path
from thejokers_app import *
urlpatterns = [
     path('', thejokers_app_view),
     path('/', thejokers_app_view),
 ]
 