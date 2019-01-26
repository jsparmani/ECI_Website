from django.urls import path
from .import views

app_name = 'complaints'

urlpatterns = [
    path('new/', views.CreateComplaint.as_view(), name="create"),
    path('list/<slug:type>/<int:const>', views.ComplaintList.as_view(), name="complaint_list"),
    path('display_all/', views.allConstStatus, name='display_all'),
    path('get_const_num', views.get_const_num, name='get_const_num'),
    path('get_type_num', views.get_type_num, name='get_type_num'),
    path('get_type', views.get_type, name='get_type'),
    path('display_const_stats/<int:const>', views.display_const_stats, name='display_const_stats'),
    path('display_type_stats/<slug:type>', views.display_type_stats, name='display_type_stats'),
    path('details/<int:pk>', views.ComplaintDetail.as_view(), name='single'),
]
