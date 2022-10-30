from django.shortcuts import render
from .models import *

# Create your views here.
projectList = [
    {
        "id": "1",
        "nombre": "valleapp",
        "descripcion": "Valle app PRO",
    },
    {
        "id": "2",
        "nombre": "direktu",
        "descripcion": "Direktu app PRO",
    },
    {
        "id": "3",
        "nombre": "Gestion Requerimientos",
        "descripcion": "Gestion Requerimientos PRO",
    }
]

def projects(request):
    projects = Project.objects.all()
    context =  {'projects': projects}
    return render(request, "projects/projects.html", context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    context = {'projectObj': projectObj}
    return render(request, "projects/single-project.html", context)
