from django import forms
from .import models
from accounts import models as acc_models


class ComplaintForm(forms.ModelForm):

    class Meta():
        model = models.Complaint
        exclude = ['user', 'created_at', 'viewed_complaint']


class get_number(forms.Form):

    const = forms.IntegerField()


class get_type_form(forms.Form):

    """ COMPLAINT_CHOICES = [
        ('Booth Capturing', 'Booth Capturing'),
        ('Bogus Voting', 'Bogus Voting'),
        ('Liquor Distribution', 'Liquor Distribution'),
        ('Money Distribution', 'Money Distribution'),
        ('Over Campaigning', 'Over Campaigning'),
        ('Obstruction to voters', 'Obstruction to voters'),
        ('No armed forces', 'No armed forces'),
        ('EVM Malfunctioning', 'EVM Malfunctioning'),
    ] """

    COMPLAINT_CHOICES = []
    type_list = [u['type'] for u in acc_models.ComplaintType.objects.all().values('type')]
    for temp in type_list:
        COMPLAINT_CHOICES.append((temp,temp))



    type = forms.ChoiceField(choices=COMPLAINT_CHOICES)


class get_type_num_form(forms.Form):

    const = forms.IntegerField(initial=0)

    select_all = forms.BooleanField(required=False)

    """ COMPLAINT_CHOICES = [
        ('All', 'All'),
        ('Booth Capturing', 'Booth Capturing'),
        ('Bogus Voting', 'Bogus Voting'),
        ('Liquor Distribution', 'Liquor Distribution'),
        ('Money Distribution', 'Money Distribution'),
        ('Over Campaigning', 'Over Campaigning'),
        ('Obstruction to voters', 'Obstruction to voters'),
        ('No armed forces', 'No armed forces'),
        ('EVM Malfunctioning', 'EVM Malfunctioning'),
    ] """

    COMPLAINT_CHOICES = [('All','All')]
    type_list = [u['type'] for u in acc_models.ComplaintType.objects.all().values('type')]
    for temp in type_list:
        COMPLAINT_CHOICES.append((temp,temp))

    type = forms.ChoiceField(choices=COMPLAINT_CHOICES)


class CommentForm(forms.ModelForm):

    class Meta():
        model = models.Comment
        fields = ('text',)
