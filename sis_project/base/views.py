from django.shortcuts import render

# Create your views here.
def base_home_view(request):
    return render(request, 'base/base.html')
