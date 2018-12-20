from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms.widgets import Select

class ProfileForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class':'form-control', 'placeholder':'example@email.com', 'required':'True'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control', 'placeholder':'Username', 'required':'True'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control', 'placeholder':'Password', 'required':'True'
        }
    ))

    class Meta():
        model = User
        fields = ('email', 'username', 'password')
