from django import forms
from .models import Listing

class ListForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = {"brand", "model", "year", "chassis_number", "mileage", "color", "engine", "transmission", "price", "image", "description"}