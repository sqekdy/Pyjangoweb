from django.http import HttpResponseRedirect
from django.contrib.auth import login 
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from django.views.generic import View
from django import template
from django.http import HttpResponse
from django.utils import timezone
import datetime
from django.views.generic import ListView
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from readyapp.models import loginForm


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            userNAME = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user= authenticate(username=userNAME, password=raw_password)
            login(request, user)
            return redirect('/SignUpConfirmation')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



class HomePageView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        now=datetime.datetime.now()
        context=super(HomePageView,self).get_context_data(**kwargs)
        context['now']=timezone.now()
        return context


class UserPageView(TemplateView):
    template_name="UserPage.html"


class SignUpConfirmationView(TemplateView):
    template_name="SignUpConfirmation.html"


    

class AboutPageView(TemplateView):
    template_name="about.html"









    
    
