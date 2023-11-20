from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are successfully logged in as { username }")
                return redirect("home")
            else:
                pass
        else:
            messages.error(request, f"Error trying to login (Check Username or Password)")
    elif request.method == "GET":
        login_form = AuthenticationForm()
        
    return render(request, "login.html", {"login_form":login_form})