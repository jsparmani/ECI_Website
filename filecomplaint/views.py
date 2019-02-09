from django.shortcuts import render
from django.views.generic import TemplateView
from accounts import models as acc_models
from complaints import models as com_models
from django.contrib.auth.models import User


class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request):
    	likes = com_models.Complaint.objects.all().filter(is_liked__iexact=1).count()
    	dislikes = com_models.Complaint.objects.all().filter(is_disliked__iexact=1).count()
    	return render(request, self.template_name, {'likes':likes, 'dislikes':dislikes})

class WelcomePage(TemplateView):
    template_name = 'welcome.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

def fault_page(request,fault):
    return render(request, 'fault.html', {'fault':fault})
