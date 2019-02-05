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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget = forms.PasswordInput)
    

