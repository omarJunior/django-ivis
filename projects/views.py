from django.shortcuts import redirect, render
from .models import *
from .forms import ProjectForm

# Create your views here.
def projects(request):
    projects = Project.objects.all().order_by('-created')
    context =  {'projects': projects}
    return render(request, "projects/projects.html", context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    context = {'projectObj': projectObj}
    return render(request, "projects/single-project.html", context)

def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)