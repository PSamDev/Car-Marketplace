from django.contrib.auth.models import User
from userapp.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

def create_user_profile(sender, instance, created, **kwargs):
    pass