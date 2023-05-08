from django.db import models
# from django.core import validators
class User(models.Model):
    name=models.CharField(max_length=60,unique=True)
    email=models.EmailField(max_length=254,unique=True)
    password=models.CharField(max_length=100,unique=True)
    