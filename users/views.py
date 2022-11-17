from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from django.contrib.auth.models import User
from django.db.models import Q
from users.models import *
from .utils import paginationProfiles, searchProfiles

# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'Username does not exist')
    
        user = authenticate(
            request = request,
            username = username,
            password = password
        )
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'profiles')
        else:
            messages.error(request,"Username or password is incorrect")
    context = {'page': page}
    return render(request, "users/login_register.html", context)

def logoutUser(request):
    logout(request)
    messages.info(request,"Username was logged out")
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == "POST":
        #registrar datos del authuser
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #create a instance
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account was created")
            login(request, user)
            return redirect('edit_account')
        else:
            messages.error(request, 'An error has occured during registration')

    context = {'page': page, 'form': form}
    return render(request, "users/login_register.html", context)

def profiles(request):
    profiles, search_query = searchProfiles(request)
    results = 1
    custom_range, profiles = paginationProfiles(request, profiles, results)
    context = {'profiles': profiles, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, "users/profiles.html", context)

def userProfile(request, pk):
    profile = Profile.objects.get(id = pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    
    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, "users/user-profile.html", context)

@login_required(login_url="login")
def userAccount(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        skills = profile.skill_set.all()
        projects = profile.project_set.all()
        context = {'profile': profile, 'skills': skills, 'projects': projects}
        return render(request, "users/account.html", context)
    return redirect('login')


@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance = profile)
    context = {'form': form}
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            user = form.save(commit=False)  #create instance
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account was updated")
            return redirect('account')
            
    return render(request, "users/profile_form.html", context)


@login_required(login_url="login")
def createSkill(request):
    form = SkillForm()
    context = {}
    context = {'form': form}
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
            messages.success(request,'Skill wass added succesfully!')
            return redirect('account')
    return render(request, "users/skill_form.html", context)


@login_required(login_url="login")
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    form = SkillForm(instance=skill) #instance of skill
    context = {}
    context = {'form': form}
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,'Skill wass updated succesfully!')
            return redirect('account')
    return render(request, "users/skill_form.html", context)


@login_required(login_url="login")
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id = pk)
    context = {'object': skill}
    if request.method == "POST":
        skill.delete()
        messages.success(request,'Skill wass deleted succesfully!')
        return redirect('account')
    return render(request, 'delete_template.html', context)