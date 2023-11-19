from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return render(request, "welcome.html", {"name":"AutoMax"})

@login_required
def home(request):
    return render(request, "home.html")