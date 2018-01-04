from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, initial="For eg., Sandip" )
    last_name = forms.CharField(max_length=30, required=False,initial="For eg., Gautam")
    email = forms.EmailField(max_length=254, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1')

