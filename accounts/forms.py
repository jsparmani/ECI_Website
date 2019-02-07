""" from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib import auth
from accounts.models import User


class  UserCreateForm(UserCreationForm):

    class Meta():
        fields = ['username', 'password1', 'password2']
        model = User """



from django import forms
from .import models
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget = forms.PasswordInput)

class AddUserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ['username', 'password']

        widgets = {'password': forms.PasswordInput}

class AddVoterForm(forms.ModelForm):

    class Meta():
        model = models.Voter
        exclude = ['user']





    
    

