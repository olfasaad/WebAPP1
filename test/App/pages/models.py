from re import T
from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    