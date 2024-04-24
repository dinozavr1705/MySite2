from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    rating = models.FloatField(max_length=3, default=0)
    skills = models.CharField(max_length=1000, default="Отсутствуют")

