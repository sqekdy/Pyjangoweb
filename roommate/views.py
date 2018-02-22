from django.http import request
from django.shortcuts import render
from .models import ExpenseForm
from .models import Expense
from . import calculateFinal
# Create your views here.

#@render(request,'Entry.html',{'form':form})
def newEntry(request):
    mycost=calculateFinal.totalExpense()
    if request.method=='POST':
        form=ExpenseForm(request.POST)
        if form.is_valid():
            form.save(commit="true")
            entry_status='true'

        else:
            print(form.errors)
    entry_status='false'
    form=ExpenseForm()



    return render(request, 'Entry.html', {'form': form, 'mycost':mycost})






