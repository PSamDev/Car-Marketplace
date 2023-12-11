import uuid
from django.db import models
from userapp . models import Profile, Location
from . import constants
from . import utils

# Create your models here.
class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50, default=None, choices=constants.CAR_BRANDS)
    model = models.CharField(max_length=150, default=None)
    chassis_number = models.CharField(max_length=50, default=None)
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=50, default="White")
    description = models.TextField(default=None)
    engine = models.CharField(max_length=50, default=None)
    transmission = models.CharField(max_length=50, default=None, choices=constants.TRANSMISSION)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to=utils.user_listing_path, max_length=None, default=None)