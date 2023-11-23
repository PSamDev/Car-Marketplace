from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.
class Register(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, "register.html", {"register_form":register_form})
    def post(self, request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request, user)
            messages.success(request, f"User {user.username} created successfully")
            return redirect("home")
        else:
            messages.error(request, f"Error trying to Register new user")
            return render(request, "register.html", {"register_form":register_form})

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

@login_required
def logout_view(request):
    logout(request)
    return redirect("welcome")
