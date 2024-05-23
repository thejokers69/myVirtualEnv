from django.shortcuts import render

def moderation_list(request):
    return render(request, 'moderation/moderation_list.html')

def moderation_detail(request, id):
    return render(request, 'moderation/moderation_detail.html', {'id': id})
