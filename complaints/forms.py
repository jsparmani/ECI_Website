from django import forms
from .import models


class ComplaintForm(forms.ModelForm):

    class Meta():
        model = models.Complaint
        exclude = ['user', 'created_at', 'viewed_complaint']


class get_number(forms.Form):

    const = forms.IntegerField()


class get_type_form(forms.Form):

    COMPLAINT_CHOICES = [
        ('Booth Capturing', 'Booth Capturing'),
        ('Bogus Voting', 'Bogus Voting'),
        ('Liquor Distribution', 'Liquor Distribution'),
        ('Money Distribution', 'Money Distribution'),
        ('Over Campaigning', 'Over Campaigning'),
        ('Obstruction to voters', 'Obstruction to voters'),
        ('No armed forces', 'No armed forces'),
        ('EVM Malfunctioning', 'EVM Malfunctioning'),
    ]

    type = forms.ChoiceField(choices=COMPLAINT_CHOICES)


class get_type_num_form(forms.Form):

    const = forms.IntegerField(initial=0)

    select_all = forms.BooleanField(required=False)

    COMPLAINT_CHOICES = [
        ('All', 'All'),
        ('Booth Capturing', 'Booth Capturing'),
        ('Bogus Voting', 'Bogus Voting'),
        ('Liquor Distribution', 'Liquor Distribution'),
        ('Money Distribution', 'Money Distribution'),
        ('Over Campaigning', 'Over Campaigning'),
        ('Obstruction to voters', 'Obstruction to voters'),
        ('No armed forces', 'No armed forces'),
        ('EVM Malfunctioning', 'EVM Malfunctioning'),
    ]

    type = forms.ChoiceField(choices=COMPLAINT_CHOICES)


class CommentForm(forms.ModelForm):

    class Meta():
        model = models.Comment
        fields = ('text',)
