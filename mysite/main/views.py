from django.shortcuts import render
from django.http import HttpResponse


def button_view(request):
        return render(request, 'main/registration.html')

def test_function(request):
    return render(request, "main/index.html")

