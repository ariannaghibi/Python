from django.forms import ModelForm, TextInput
from .models import City


# This class is created to replace the original textbox input in the weather app and to allow us to add our own functionality
class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'type': 'text', 'placeholder': 'City Name'})}

