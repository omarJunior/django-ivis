from django.shortcuts import render
from users.models import *

# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, "users/profiles.html", context)
    