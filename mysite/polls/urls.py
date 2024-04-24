from django.urls import path

from . import views

urlpatterns = [
    path("registration/", views.new_user, name="registration"),
    path("login/", views.loginuser, name="login"),
    path("profile/",views.profile, name = "profile"),
    path("profiles/",views.list_of_profiles,name = "list_of_profiles")
]
