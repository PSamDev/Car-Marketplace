from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Listing
from . forms import ListForm
from userapp.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def welcome(request):
    return render(request, "welcome.html", {"name":"AutoMax"})

@login_required
def home(request):
    listing = Listing.objects.all()
    items_per_page = 6 

    #fix pagination
    paginator = Paginator(listing, items_per_page)
    page = request.GET.get('page')

    try:
        listing_page = paginator.page(page)
    except PageNotAnInteger:
        listing_page = paginator.page(1)
    except EmptyPage:
        listing_page = paginator.page(paginator.num_pages)
                                      
    listingfilter = ListingFilter(request.GET, queryset=listing)
    context = {"listingfilter":listingfilter, "listing_page":listing_page}

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
    
@login_required
def carinfo(request, id):
   try:
       carinfo=Listing.objects.get(id=id)
       if carinfo == None:
           raise Exception
       return render(request, "carinfo.html", {"carinfo":carinfo})
   except Exception as e:
       messages.error(request, f"Invalid UUID {id} provided")
       return redirect("home")
   