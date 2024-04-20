from django.shortcuts import render
from django.http import HttpResponse
import json
import sqlite3
from sqlite3 import  *
def test_function(request):
    return HttpResponse(request,'<h3>Регистрация</h3>')
def func(request):
    return render(request,'main/registration.html')
def login(request):
    return render(request, 'main/login.html')




def new_user(request):
    if request.method == 'post':
        name = request.POST.get('login')
        password = request.POST.get('password')
        db = sqlite3.connect("db.sqlite3")
        c = db.cursor()
        ID = request.user.id
        if name and password:
            c.execute("INSERT INTO  auth_user Values(ID,password,datetime.today,False,'','',False,True,datetime.today,'')")
        db.close()
