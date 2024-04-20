from django.shortcuts import render
from django.http import HttpResponse

def custom_function():
    return "Функция была успешно вызвана!"

def button_view(request):
        return render(request, 'registration.html')

def func(request):
    return  render(request,'registration.html')
def test_function(request):
    return render(request, "main/index.html")
