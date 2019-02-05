from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

# Create your models here.

""" class User(auth.Models.User, auth.Models.PermissionsMixin):

    
    
    def __str__(self):
        return self.username
 """

 



class Voter(models.Model):
    user = models.OneToOneField(
        User, related_name="voter_details", on_delete=models.CASCADE)
    cons_no = models.PositiveIntegerField(blank=False)
    booth_no = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.user.username


class Constituency(models.Model):
    booth = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.pk) 


class ComplaintType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class GovUser(models.Model):
    user = models.OneToOneField(User, related_name="gov", on_delete=models.CASCADE)
    # govname = models.CharField(max_length=30, default = GovUser.gov.user.username)

    def __str__(self):
        return self.user.username
