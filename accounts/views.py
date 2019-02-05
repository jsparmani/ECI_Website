from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .import forms
from django.http import HttpResponse

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






