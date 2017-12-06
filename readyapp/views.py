from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django import template
from django.http import HttpResponse
from django.utils import timezone
import datetime
from django.views.generic import ListView
from readyapp.models import EmployeeInput

# Create your views here.



class HomePageView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        now=datetime.datetime.now()
        context=super(HomePageView,self).get_context_data(**kwargs)
        context['now']=timezone.now()
        return context
    

class AboutPageView(TemplateView):
    template_name="about.html"


class EmployeeView(ListView):
    model=EmployeeInput

    
    
