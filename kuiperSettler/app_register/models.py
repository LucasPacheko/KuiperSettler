from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    email = models.TextField(max_length=255, unique=True)
    password = models.TextField(max_length=255)
