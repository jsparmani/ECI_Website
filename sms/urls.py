from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from .import views

app_name = 'sms'


urlpatterns = [
    path('send/<slug:complaint_type>/<int:msg_type>/<slug:name>/<int:phone_num>/', views.send, name='send'),
    

]
