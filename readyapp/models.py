from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm# change in here

# Create your models here.

#We need to define the page for the employee input


class UserForm(UserCreationForm):
    #user_password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=('username', 'email', 'password1','password2')

class loginForm(UserCreationForm):
    #user_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','password1')
        


    
