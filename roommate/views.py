from django.shortcuts import render
from .models import ExpenseForm
# Create your views here.

def newEntry(request):
    if request.method=='POST':
        form=ExpenseForm(request.POST)
        if form.is_valid():
            form.save(commit="true")
            entry_status='true'

        else:
            print(form.errors)
    entry_status='false'
    form=ExpenseForm()

    return render(request, 'Entry.html', {'form': form})



