from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .import forms
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .import models

# Create your views here.

def login(request):
    if request.method=='POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('welcome')
            else:
                return HttpResponse("Invalid!!!!!!")
    else:
        form = forms.LoginForm()
    return render(request, 'accounts/login.html', {'form':form})

def add_user(request):
    if request.method == 'POST':
        form = forms.AddUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # password2 = form.cleaned_data['password2']
            try:
                temp = User.objects.get(username=username)
            except:
                user = User.objects.create_user(username, '', password)
                user.save()
                return redirect('accounts:add_voter',username=username)
        return HttpResponse("User with this username already exists")

    else:
        form = forms.AddUserForm()
        return render(request, 'accounts/add_user.html', {'form':form})


def add_voter(request, username):
    if request.method == 'POST':
        form = forms.AddVoterForm(request.POST)
        if form.is_valid():
            voter = form.save(commit=False)
            voter.user = User.objects.get(username=username)
            voter.save()
            form = forms.AddUserForm()
            return redirect('accounts:add_user')
            

    else:
        form = forms.AddVoterForm()
        return render(request, 'accounts/add_voter.html', {'form':form,'username':username})


def add_gov_user(request):
    if request.method == 'POST':
        form = forms.AddUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                temp = User.objects.get(username=username)
            except:
                user = User.objects.create_user(username, '', password)
                user.save()
                gov_user = models.GovUser.objects.create(user=user)
                form = forms.AddUserForm()
                return render(request,'accounts/add_gov_user.html',{'form':form})
                
        return HttpResponse("User with this username already exists")
    else:
        form = forms.AddUserForm()
    return render(request, 'accounts/add_gov_user.html', {'form':form})


                    






