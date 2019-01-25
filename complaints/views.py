from django.shortcuts import render, redirect
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


def allConstStatus(request):
    booth_capturing_num = models.Complaint.objects.all().filter(
        choice__iexact="Booth Capturing").count()
    bogus_voting_num = models.Complaint.objects.all().filter(
        choice__iexact="Bogus Voting").count()
    liquor_distribution_num = models.Complaint.objects.all().filter(
        choice__iexact="Liquor Distribution").count()
    money_distribution_num = models.Complaint.objects.all().filter(
        choice__iexact="Money Distribution").count()
    over_campaigning_num = models.Complaint.objects.all().filter(
        choice__iexact="Over Campaigning").count()
    obstruction_voters_num = models.Complaint.objects.all().filter(
        choice__iexact="Obstruction to voters").count()
    armed_forces_num = models.Complaint.objects.all().filter(
        choice__iexact="No armed forces").count()
    evm_malfunctioning_num = models.Complaint.objects.all().filter(
        choice__iexact="EVM Malfunctioning").count()
    dict = {'booth_capturing_num': booth_capturing_num,
            'bogus_voting_num': bogus_voting_num,
            'liquor_distribution_num': liquor_distribution_num,
            'money_distribution_num': money_distribution_num,
            'over_campaigning_num': over_campaigning_num,
            'obstruction_voters_num': obstruction_voters_num,
            'armed_forces_num': armed_forces_num,
            'evm_malfunctioning_num': evm_malfunctioning_num}
    return render(request, 'complaint/display_all_stats.html', context=dict)


def get_const_num(request):
    if request.method == 'POST':
        form = forms.get_number(request.POST)
        if form.is_valid():
            const = form.cleaned_data['const']
            return redirect('complaints:display_const_stats', const=const)
        # const = request.POST['const']
    else:
        form = forms.get_number()
    return render(request, 'complaint/get_constituency.html', {'form':form})


def display_const_stats(request, const):
    booth_capturing_num = models.Complaint.objects.all().filter(
        choice__iexact="Booth Capturing", user__voter_details__cons_no__iexact=const).count()
    bogus_voting_num = models.Complaint.objects.all().filter(
        choice__iexact="Bogus Voting", user__voter_details__cons_no__iexact=const).count()
    liquor_distribution_num = models.Complaint.objects.all().filter(
        choice__iexact="Liquor Distribution", user__voter_details__cons_no__iexact=const).count()
    money_distribution_num = models.Complaint.objects.all().filter(
        choice__iexact="Money Distribution", user__voter_details__cons_no__iexact=const).count()
    over_campaigning_num = models.Complaint.objects.all().filter(
        choice__iexact="Over Campaigning", user__voter_details__cons_no__iexact=const).count()
    obstruction_voters_num = models.Complaint.objects.all().filter(
        choice__iexact="Obstruction to voters", user__voter_details__cons_no__iexact=const).count()
    armed_forces_num = models.Complaint.objects.all().filter(
        choice__iexact="No armed forces", user__voter_details__cons_no__iexact=const).count()
    evm_malfunctioning_num = models.Complaint.objects.all().filter(
        choice__iexact="EVM Malfunctioning", user__voter_details__cons_no__iexact=const).count()
    dict = {'const': const, 
            'booth_capturing_num': booth_capturing_num,
            'bogus_voting_num': bogus_voting_num,
            'liquor_distribution_num': liquor_distribution_num,
            'money_distribution_num': money_distribution_num,
            'over_campaigning_num': over_campaigning_num,
            'obstruction_voters_num': obstruction_voters_num,
            'armed_forces_num': armed_forces_num,
            'evm_malfunctioning_num': evm_malfunctioning_num}
    return render(request, 'complaint/display_const_stats.html', context=dict)
