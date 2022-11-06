#https://github.com/divanov11/Django-2021
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProjectForm

# Create your views here.
def projects(request):
    projects = Project.objects.all().order_by('-created')
    c_project = projects.count()
    context =  {'projects': projects, 'count': c_project}
    return render(request, "projects/projects.html", context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    context = {'project': projectObj}
    return render(request, "projects/single-project.html", context)

@login_required(login_url="login")
def createProject(request):
    #add project
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def updateProject(request, pk):
    project = Project.objects.get(id = pk)
    form = ProjectForm(instance = project) #get data instance
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id = pk)
    context = {'object': project}
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete_template.html', context)
