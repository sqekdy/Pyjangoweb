from django.db import models
from django.forms import ModelForm

# Create your models here.

#We need to define the page for the employee input

class EmployeeInput(models.Model):
    employee_name=models.CharField(max_length=20)
    employee_number= models.CharField(max_length=10)
    employee_email=models.CharField(max_length=30)

    class Meta:
        db_table="employeedetails"

    def __str__(self):
        return self.employee_name



class UserCredentials(models.Model):
    user_name=models.CharField(max_length=20)
    user_email=models.CharField(max_length=20)
    user_password=models.CharField(max_length=20)

    class Meta:
        db_table="userdetails"

    def __str__(self):
        return (self.user_name)

class UserForm(ModelForm):
    class Meta:
        model=UserCredentials
        fields=['user_name', 'user_email', 'user_password']

class loginForm(ModelForm):
    class Meta:
        model=UserCredentials
        fields=['user_name','user_password']
        


    
