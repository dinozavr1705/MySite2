from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, PasswordInput

from .models import User


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Логин'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Пароль'}))