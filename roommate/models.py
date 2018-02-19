from django.db import models
from roommate import ExpenseForm
from django.forms import ModelForm
# Create your models here.

# We define a model (database and the fields, using Expense Class, then we create a form using that model fields
class Expense(models.Model):

    Entry_Number=models.AutoField(primary_key='true')
    Entry_Made_By= models.CharField(max_length=20)
    Entry_Date=models.DateTimeField()
    Amount=models.IntegerField()
    Description=models.TextField(max_length=500)


class ExpenseForm(ModelForm):
    class Meta:
        model=Expense
        fields=['Entry_Made_By','Entry_Date','Amount','Description']







