#readyapp/urls.py

from django.conf.urls import url
from readyapp import views
from readyapp.views import signup
from readyapp.views import login
from django.contrib.auth import views as auth_views


urlpatterns=[
    url(r'^$',views.HomePageView.as_view()),
    url(r'^about/$',views.AboutPageView.as_view()),
    #url(r'^time/$', current_datetime), No need , displaying in home page
    url(r'^input/$',views.EmployeeView.as_view()),
    url(r'^signup/$',signup, name="signup"),
    url(r'^UserPage/$',views.UserPageView.as_view()),
    url(r'^SignUpConfirmation/$',views.SignUpConfirmationView.as_view()),
    url(r'^login/$',login,name="login"),
    ]
