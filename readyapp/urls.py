#readyapp/urls.py

from django.conf.urls import url
from readyapp import views

urlpatterns=[
    url(r'^$',views.HomePageView.as_view()),
    url(r'^about/$',views.AboutPageView.as_view()),
    #url(r'^time/$', current_datetime), No need , displaying in home page
    url(r'^input/$',views.EmployeeView.as_view()),
    ]