from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    # path('login/',auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('login/', views.login, name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name = 'logout'),
    path('add_user/',views.add_user,name='add_user'),
    path('add_voter/<str:username>/',views.add_voter,name='add_voter'),
    path('add_gov_user/',views.add_gov_user,name='add_gov_user'),
]