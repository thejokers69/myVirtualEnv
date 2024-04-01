from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Program
from django.urls import reverse_lazy

# Define views here

def prog_home_view(request):
    # Define the view logic here
    pass

def prog_edit_success(request):
    # Define the view logic here
    pass

def prog_delete_success(request):
    # Define the view logic here
    pass

class ProgramListView(ListView):
    model = Program
    template_name = 'program/prog_list.html'

class ProgramCreateView(CreateView):
    model = Program
    template_name = 'program/prog_edit_form.html'
    success_url = reverse_lazy('prog-create-success')

class ProgramUpdateView(UpdateView):
    model = Program
    template_name = 'program/prog_edit_form.html'
    success_url = reverse_lazy('prog-edit-success')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program/prog_confirm_delete.html'
    success_url = reverse_lazy('prog-delete-success')

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program/prog_detail.html'
