from django import forms
from .models import Location, Profile
from .widgets import CustomPictureImageFieldWidget
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=CustomPictureImageFieldWidget)
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = {"profile_image", "bio", "phone_number"}

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = {"state", "city", "zip_code", "address"}