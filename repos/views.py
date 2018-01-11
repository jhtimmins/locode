import json
from .models import Repo
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from services import queue, repo


def home(request):
    """
    LOCode home page.
    """
    return render(request, 'repos/home.html')


def search(request):
    """
    Search for repo data and queue if not found.
    """
    validated_repo = repo.validate(request.GET['route'])
    if not validated_repo:
        return JsonResponse({'status': 'invalid'})

    try:
        result = Repo.objects.get(path=validated_repo)
        render = render_to_string("repos/results.html", {'results': json.loads(result.details)})
        return HttpResponse(render)
    except Repo.DoesNotExist:
        queue.queue_repo(validated_repo)
        return JsonResponse({'status': 'queued'})
