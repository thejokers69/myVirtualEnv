from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Program

class ProgramListView(ListView):
    queryset = Program.objects.all()
    paginate_by = 10
    template_name = 'program/prog_list.html'
    context_object_name = 'program_list'

class ProgramDetailView(DetailView):
   model = Program
   template_name = 'program/prog_detail.html'
   context_object_name = 'program' 

class ProgramFormMixin:
    model = Program
    fields = ['prog_name', 'prog_description', 'registration_fees']
    template_name = 'program/prog_edit.html'
    success_url = '/program/edit/success/'

class ProgramCreateView(ProgramFormMixin, CreateView):
    pass

class ProgramUpdateView(ProgramFormMixin, UpdateView):
    pass

class ProgramDeleteView(DeleteView):
   model = Program
   template_name = 'program/prog_confirm_delete.html'
   success_url = reverse_lazy('prog-list')  # URL to redirect to upon successful form submission



# Create your views here.
def prog_home_view(request):
    return render(request, 'program/index.html')

# Program edit success
def prog_edit_success(request):
    return render(request, 'program/prog_edit_success.html')

# Program delete success
def prog_delete_success(request):
    return render(request, 'program/prog_delete_success.html')