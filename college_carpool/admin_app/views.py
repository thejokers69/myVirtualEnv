from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .forms import UserUpdateForm
from .models import Report, Comment
from passenger_app.models import Trip  # Add this import

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin_app/manage_users.html', {'users': users})

@user_passes_test(is_admin)
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserCreationForm()
    return render(request, 'admin_app/create_user.html', {'form': form})

@user_passes_test(is_admin)
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'admin_app/update_user.html', {'form': form})

@user_passes_test(is_admin)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('manage_users')
    return render(request, 'admin_app/delete_user.html', {'user': user})

@user_passes_test(is_admin)
def moderate_comments(request):
    comments = Comment.objects.all()
    return render(request, 'admin_app/moderate_comments.html', {'comments': comments})

@user_passes_test(is_admin)
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('moderate_comments')
    return render(request, 'admin_app/delete_comment.html', {'comment': comment})

@user_passes_test(is_admin)
def generate_reports(request):
    total_users = User.objects.count()
    total_trips = Trip.objects.count()
    report = Report.objects.create(total_users=total_users, total_trips=total_trips)
    reports = Report.objects.all()
    return render(request, 'admin_app/reports.html', {'reports': reports})
