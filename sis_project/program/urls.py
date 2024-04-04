from django.urls import path
from program.views import (
        ProgramListView,
        prog_home_view,
        prog_edit_success,
        prog_delete_success,
        ProgramCreateView,
        ProgramUpdateView, 
        ProgramDeleteView,
        ProgramDetailView,       
    )

urlpatterns = [
    path('', prog_home_view, name='program-home'),
    path('list/', ProgramListView.as_view(), name='prog-list'),
    path('detail/<int:pk>/', ProgramDetailView.as_view(), name='prog-detail'),
    path('edit/', ProgramCreateView.as_view(), name='prog-edit'),
    path('edit/<int:pk>/', ProgramUpdateView.as_view(), name='prog-edit'),
    path('delete/<int:pk>/', ProgramDeleteView.as_view(), name='prog-delete'),
    path('edit/success/', prog_edit_success, name='prog-create-success'),
    path('edit/<int:pk>/success/', prog_edit_success, name='prog-edit-success'),
    path('delete/success/', prog_delete_success, name='prog-delete-success'),
]