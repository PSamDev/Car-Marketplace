from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Listing
from . forms import ListForm
from userapp.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter

# Create your views here.
def welcome(request):
    return render(request, "welcome.html", {"name":"AutoMax"})

@login_required
def home(request):
    listing = Listing.objects.all()
    listingfilter = ListingFilter(request.GET, queryset=listing)
    context = {"listingfilter":listingfilter}
    return render(request, "home.html", context)

@login_required
def list_form(request):
    if request.method == "POST":
        try:
            listingform=ListForm(request.POST, request.FILES) 
            locationform=LocationForm(request.POST)
            if listingform.is_valid() and locationform.is_valid():
                listing = listingform.save(commit=False)
                listinglocation = locationform.save()
                listing.seller = request.user.profile
                listing.location = listinglocation
                listing.save()
                messages.success(request, f"Congratulations {request.user.username} your car has been listed for sale!")
                return redirect("home")
            else:
                Exception
        except Exception as e:
            print(e)
            messages.error(request, "We encountered an error Listing your car. Please Try Again")
    else:
        listingform = ListForm()
        locationform=LocationForm()
        return render (request, "list_form.html", {"listform":listingform, "locationform":locationform})