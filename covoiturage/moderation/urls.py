from django.urls import path
from . import views

urlpatterns = [
    path('', views.moderation_list, name='moderation_list'),
    path('<int:id>/', views.moderation_detail, name='moderation_detail'),
]
