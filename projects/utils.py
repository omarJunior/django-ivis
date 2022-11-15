from .models import *
from django.db.models import Q

def searchProjects(request):
    search_query = ""
    if request.GET.get('searchQuery'):
        search_query = request.GET.get('searchQuery')

    tags = Tag.objects.filter(name__icontains = search_query)
    projects = Project.objects.distinct().filter(
        Q(owner__name__icontains = search_query)|
        Q(title__icontains = search_query)|
        Q(description__icontains = search_query)|
        Q(tags__in = tags))

    return projects, search_query