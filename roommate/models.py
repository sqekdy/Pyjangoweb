from django.db import models
from roommate import ExpenseForm
from django.forms import ModelForm
from django import forms
# Create your models here.

# We define a model (database and the fields, using Expense Class, then we create a form using that model fields
class Expense(models.Model):

    Entry_Number=models.AutoField(primary_key='true')
    Entry_Made_By= models.CharField(max_length=20)
    Entry_Date=models.DateField(auto_now=True)
    Amount=models.IntegerField()
    Description=models.TextField(max_length=500)

    def __str__(self):
        return '%s, %s %s' %(self.Amount, self.Entry_Made_By,self.Entry_Date)

class ExpenseForm(ModelForm):
    class Meta:
        model=Expense
        fields=['Entry_Made_By','Amount','Description']







