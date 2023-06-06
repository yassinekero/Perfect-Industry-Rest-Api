from django.db import models
from django.contrib.auth.models import AbstractUser



class Admin(AbstractUser):
    login = models.CharField(max_length=(250), unique=True)
    password = models.CharField(max_length=250)

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = []

# Create your models here.
