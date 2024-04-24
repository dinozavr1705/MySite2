from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import sqlite3
from sqlite3 import *
from django.contrib.auth.urls import *
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm
from .models import User


def profile(request):
    return render(request,'main/profile.html',{"description":User.skills})


def func(request):
    return render(request, 'main/registration.html')




def new_user(request):
    form = UserForm()
    if request.method == 'POST':
        if form.is_valid():
            name = request.POST.get('username')
            password = request.POST.get('password')
            # skills = request.POST.get('skills').split()
            form.save()
            username = form.cleaned_data.get('username')
            newuser = User.objects.create(username=name, password=password, rating=0)
            print(newuser)
            newuser.save()
            login(request, newuser)
        else:
            form = UserForm()
    return render(request, 'main/registration/registration.html', {'form': form })

def list_of_profiles(request):
    a = QuerySet.iterator
    print(a)
    return render(request,"main/page_of_profiles.html",{"a":a})

def loginuser(request):
    if request.method == "post":
        return render(request, 'registration/login.html', {"form": AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html',
                          {"form": AuthenticationForm(),
                           'error': "Invalid login credentials!"})
        else:
            login(request, user)

def test_func(request):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    rows = cursor.fetchall()
    a = ""

