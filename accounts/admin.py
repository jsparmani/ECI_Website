from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.Voter)
admin.site.register(models.Constituency)
admin.site.register(models.ComplaintType)
admin.site.register(models.GovUser)
