from django.conf.urls import url
from roommate import views
from roommate.views import newEntry

urlpatterns=[
    url(r'^userPage/newEntry/$',newEntry,name='newEntry'),

    ]
