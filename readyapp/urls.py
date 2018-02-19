#readyapp/urls.py

from django.conf.urls import url
from readyapp import views
from readyapp.views import signup
from django.contrib.auth import views as auth_views



urlpatterns=[
    url(r'^$',views.HomePageView.as_view()),
    url(r'^about/$',views.AboutPageView.as_view()),
    #url(r'^time/$', current_datetime), No need , displaying in home page
    url(r'^signup/$',signup, name="signup"),
    url(r'^userPage/$',views.UserPageView.as_view()),
    url(r'^SignUpConfirmation/$',views.SignUpConfirmationView.as_view()),
    url(r'^login/$',auth_views.login,{'template_name':'login.html'}, name='login'),
    ]
