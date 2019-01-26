from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Complaint(models.Model):

    user = models.ForeignKey(
        User, related_name='complaints', on_delete=models.CASCADE)
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

    choice = models.CharField(
        max_length=50, choices=COMPLAINT_CHOICES, blank=False)
    description = models.TextField(blank=True)
    file_upload = models.FileField(
        upload_to='files', blank=True)
    file_upload1 = models.FileField(
        upload_to='files', blank=True)
    file_upload2 = models.FileField(
        upload_to='files', blank=True)
    file_upload3 = models.FileField(
        upload_to='files', blank=True)
    file_upload4 = models.FileField(
        upload_to='files', blank=True)
    file_upload5 = models.FileField(
        upload_to='files', blank=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice

    def get_absolute_url(self):
        return reverse('home')

    class Meta():
        ordering = ['created_at']
        unique_together = ["user", "choice"]
