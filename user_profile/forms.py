from .models import Profile
from django.forms import ModelForm, TextInput


class ProfileCityForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user_city']
        widgets = {'user_city': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Choose your city'
        })}