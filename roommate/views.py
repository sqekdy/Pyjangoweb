from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView   #Used for class based views
from .models import ExpenseForm
from .models import Expense
from . import calculateFinal
from .models import RoomForm
from django.views.generic import FormView
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



    return render(request, 'createRoom.html', {'form': form, 'mycost':mycost})

def newRoom(request):
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save(commit="true")

        else:
            print(form.errors)

    form=RoomForm()

    return render(request,'createRoom.html',{'form':form})

class RoomView(TemplateView):
    template_name = 'createRoom.html'

    # Passing context to the view, context, is generally the elements that we want to pass to the template
    # mentionde above

    def get(self, request, *args, **kwargs):

        form_for_expense=ExpenseForm(self.request.GET or None)
        form_for_room=RoomForm(self.request.GET or None)
        context=self.get_context_data(**kwargs)
        context['ExpenseContext']=form_for_expense
        context['RoomContext']=form_for_room
        return  self.render_to_response(context)



class ExpenseFormView(FormView):
    form_class=ExpenseForm
    template_name = 'Entry.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        Exform=self.form_class(request.POST)
        if Exform.is_valid():
            Exform.save(commit="true")
            entry_status = 'true'
            return self.render_to_response(self.get_context_data(success= True))


        else:
            return self.render_to_response(self.get_context_data(form=Exform))

















