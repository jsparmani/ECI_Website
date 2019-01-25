from django.urls import path
from .import views

app_name = 'complaints'

urlpatterns = [
    path('', views.CreateComplaint.as_view(), name="create")
]
