import uuid
from django.db import models
from userapp . models import Profile

# Create your models here.
class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)