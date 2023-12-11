from django.db import models
from django.contrib.auth.models import User

#Download django localflavor to have access to autodetection of states, zip_code etc. Load on the settings.py file too
# from localflavor.us.models import USPostalCodeField, USStateField, USSocialSecurityNumberField, USZipCodeField

# Create your models here.
    # Working with countries that are available on the django localflavor
    # state = USStateField(default = "NY")
    # zip_code = USZipCodeField(default="NY")

   
from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)  
    zip_code = models.CharField(max_length=10)  
    address = models.CharField(max_length=100) 

    def __str__(self):
        return f"{self.state}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/')  # Set upload_to directory
    bio = models.CharField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user}'s Profile"
 
