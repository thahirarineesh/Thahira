from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.
class Bank(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class img(models.Model):
    img=models.ImageField(upload_to='pics')



class About(models.Model):
    name  = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    desc1 = models.TextField()
    desc2 = models.TextField()

    def __str__(self):
        return self.name



class login(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


    def __str__(self):
     return self.name

class Register(models.Model):
    username=models.CharField(max_length=250)
    password=models.IntegerField()
    password1=models.IntegerField()

    def __str__(self):
        return self.name

