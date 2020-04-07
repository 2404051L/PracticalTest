from django.shortcuts import render

from .models import Story

def index(request):
    latest_story_list = Story.objects.order_by('-published_date')[:5]
    context = {'latest_story_list': latest_story_list}
    return render(request, 'news/index.html', context)
