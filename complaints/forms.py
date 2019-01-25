from django import forms
from .import models


class ComplaintForm(forms.ModelForm):

    class Meta():
        model = models.Complaint
        exclude = ['user', 'created_at']

class get_number(forms.Form):

    const=forms.IntegerField()


