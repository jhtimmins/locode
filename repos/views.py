from django.shortcuts import render
from django.http import JsonResponse
from services import queue, repo


def home(request):
    return render(request, 'repos/home.html')


def search(request):
    validated_repo = repo.validate(request.GET['route'])
    if validated_repo:
        message = 'success {}'.format(validated_repo)
        queue.send_message(validated_repo)
    else:
        message = 'bad repo'
    return JsonResponse({'success': message})
