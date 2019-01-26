from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .import models
from .import forms
from django.utils.text import slugify
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

# All Data Display for the country


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

# Get The Constitunecy number to display stats


def get_const_num(request):
    if request.method == 'POST':
        form = forms.get_number(request.POST)
        if form.is_valid():
            const = form.cleaned_data['const']
            return redirect('complaints:display_const_stats', const=const)
        # const = request.POST['const']
    else:
        form = forms.get_number()
    return render(request, 'complaint/get_constituency.html', {'form': form})

# Get The type of complaint to display stats


def get_type(request):
    if request.method == 'POST':
        form = forms.get_type_form(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            type = slugify(type)
            return redirect('complaints:display_type_stats', type=type)
        # const = request.POST['const']
    else:
        form = forms.get_type_form()
    return render(request, 'complaint/get_complaint_type.html', {'form': form})

def get_type_num(request):
    if request.method == 'POST':
        form = forms.get_type_num_form(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            type = slugify(type)
            const = form.cleaned_data['const']
            select_all = form.cleaned_data['select_all']
            select_all = int(select_all)
            return redirect('complaints:complaint_list', type=type, const=const, select_all=select_all)
        # const = request.POST['const']
    else:
        form = forms.get_type_num_form()
    return render(request, 'complaint/get_complaint_type_num.html', {'form': form})


# Display stats of a particular constituency

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

#  Display stats of a particular type


def display_type_stats(request, type):
    dict = {}

    type = type.replace("-", " ")

    for i in range(1, 10):
        const = models.Complaint.objects.all().filter(
            choice__iexact=type, user__voter_details__cons_no__iexact=i).count()
        dict.update({i: const})
    return render(request, 'complaint/display_type_stats.html', {'dict': dict})

# Display stats for govt

class ComplaintList(generic.ListView, LoginRequiredMixin):
    model = models.Complaint
    template_name = 'complaint/complaint_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        type_new = self.kwargs.get("type").replace("-", " ")
        select_all = self.kwargs.get("select_all")
        if type_new=='all' and select_all==0:
            return queryset.filter(user__voter_details__cons_no__iexact=self.kwargs.get("const"))

        if type_new=='all' and select_all==1:
            return queryset
        
        if type_new!='all' and select_all==1:
            return queryset.filter(choice__iexact=type_new)
        
        
        return queryset.filter(choice__iexact=type_new, user__voter_details__cons_no__iexact=self.kwargs.get("const"))
        

class ComplaintDetail(generic.DetailView, LoginRequiredMixin):
    model = models.Complaint
    template_name = 'complaint/complaint_detail.html'


