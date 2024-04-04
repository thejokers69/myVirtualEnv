from django.shortcuts import render

# Create your views here.
# Create your views here.
def std_home_view(request):
    return render(request, 'student/index.html')

