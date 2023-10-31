from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to=None, height_field=None, width_field=None, max_length=None)
    bio = models.CharField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s Profile"
    