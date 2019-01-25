from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Voter(models.Model):
    user = models.OneToOneField(User, related_name ="voter_details" ,on_delete = models.CASCADE)
    cons_no = models.PositiveIntegerField(blank = False)
    booth_no = models.PositiveIntegerField(blank = False)


    def __str__(self):
        return self.user.username