from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .import models
from .import forms
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


class CreateComplaint(LoginRequiredMixin, generic.FormView):
    template_name = 'complaint/complaint_form.html'
    form_class = forms.ComplaintForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
