#https://github.com/divanov11/Django-2021
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from .forms import ProjectForm

# Create your views here.
def projects(request):
    search_query = ""
    if request.GET.get('searchQuery'):
        search_query = request.GET.get('searchQuery')

    tags = Tag.objects.filter(name__icontains = search_query)
    
    projects = Project.objects.distinct().filter(
        Q(title__icontains = search_query)|
        Q(description__icontains = search_query)|
        Q(tags__in = tags)
        )
    context =  {'projects': projects}
    return render(request, "projects/projects.html", context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    context = {'project': projectObj}
    return render(request, "projects/single-project.html", context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False) #instance of project
            project.owner = profile
            project.title = project.title.title()
            project.save()
            #save many to many relationship
            form.save_m2m()
            messages.success(request,'Project wass added succesfully!')
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance = project) #get data instance
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            messages.success(request,'Project wass updated succesfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    context = {'object': project}
    if request.method == "POST":
        project.delete()
        messages.success(request,'Project wass deleted succesfully!')
        return redirect('account')
    return render(request, 'delete_template.html', context)
