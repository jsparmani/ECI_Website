from django.shortcuts import render
from django.views.generic import TemplateView
from accounts import models as acc_models
from django.contrib.auth.models import User


class HomePage(TemplateView):
    template_name = 'index.html'

""" 
def HomePage(request):
    id_list = [u['user'] for u in acc_models.GovUser.objects.all().values('user')]
    govname_list=[]
    for num in id_list:
        temp = User.objects.get(id__iexact = num)
        temp_name = temp.username
        govname_list.append(temp_name)

    return render(request, 'index.html', {'govname_list':govname_list})
 """
class WelcomePage(TemplateView):
    template_name = 'welcome.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
