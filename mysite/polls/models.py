from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
        password = models.CharField(max_length= 20)
        username = models.CharField(max_length= 20)




