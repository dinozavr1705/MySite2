from django.urls import path

from . import views

urlpatterns = [
    path("registration/", views.new_user, name="registration"),
    path("login/", views.login, name="login")
]
