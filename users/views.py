from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def profiles(request):
    context = {}
    return render(request, "users/profiles.html", context)
    