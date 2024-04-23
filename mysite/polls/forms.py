from django import forms
from .models import User


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
