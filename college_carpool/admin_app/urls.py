from django.urls import path
from . import views

urlpatterns = [
    path('manage_users/', views.manage_users, name='manage_users'),
    path('create_user/', views.create_user, name='create_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('moderate_comments/', views.moderate_comments, name='moderate_comments'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('generate_reports/', views.generate_reports, name='generate_reports'),
]
