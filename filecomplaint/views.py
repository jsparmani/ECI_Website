from django.shortcuts import render
from django.views.generic import TemplateView
from accounts import models as acc_models
from django.contrib.auth.models import User


class HomePage(TemplateView):
    template_name = 'index.html'

class WelcomePage(TemplateView):
    template_name = 'welcome.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

def fault_page(request,fault):
    return render(request, 'fault.html', {'fault':fault})
