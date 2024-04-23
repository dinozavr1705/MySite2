from django.shortcuts import render
from django.http import HttpResponse
import json
import sqlite3
from sqlite3 import *

from .forms import UserForm
from .models import User


def test_function(request):
    return HttpResponse(request, '<h3>Регистрация</h3>')


def func(request):
    return render(request, 'main/registration.html')


def login(request):
    return render(request, 'main/login.html')


def new_user(request):
    form = UserForm()
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        # skills = request.POST.get('skills').split()
        newuser = User.objects.create(username=name, password=password, rating=0)
        print(newuser)
    return render(request, 'main/registration/registration.html', {'form': form, })
