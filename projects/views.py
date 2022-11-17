#https://github.com/divanov11/Django-2021
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProjectForm, ReviewForm
from .utils import paginationProjects, searchProjects

# Create your views here.
def projects(request):
    projects, search_query = searchProjects(request)
    results = 6
    custom_range, projects = paginationProjects(request, projects, results)
    context =  {'projects': projects, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, "projects/projects.html", context)

@login_required(login_url="login")
def project(request, pk):
    profile = request.user.profile
    projectObj = Project.objects.get(id = pk)
    form = ReviewForm()
    if request.method == "POST":
        if Review.objects.filter(owner = profile, project=projectObj).count() > 0:
            messages.success(request,'There is already a message from you, please edit!') 
            return redirect('project', pk = pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            rewiew = form.save(commit=False)
            rewiew.owner = profile
            rewiew.project = projectObj
            rewiew.save()
            projectObj.getVoteCount
            messages.success(request,'Message wass added succesfully!')
            return redirect('project', pk = pk)

    context = {'project': projectObj, 'form': form}
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
            return redirect('account')

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
