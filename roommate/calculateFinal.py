from .models import Expense
from django.db.models import Sum

def totalExpense():

    return Expense.objects.aggregate(Sum('Amount'))



