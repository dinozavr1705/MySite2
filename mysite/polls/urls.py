from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .forms import CustomAuthForm
from . import views

urlpatterns = [
    path("registration/", views.new_user, name="registration"),
    #path(path('login',  auth_views.LoginView.as_view(template_name='main/registration/login.html', authentication_form=CustomAuthForm),
         #name='login')),
    path("profile/",views.profile, name = "profile"),
    path("profiles/",views.list_of_profiles,name = "list_of_profiles"),
    path("list_of_all_users/",views.user_list, name = "userlist")
]

