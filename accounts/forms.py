""" from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib import auth
from accounts.models import User


class  UserCreateForm(UserCreationForm):

    class Meta():
        fields = ['username', 'password1', 'password2']
        model = User """

    

