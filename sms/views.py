from django.shortcuts import render
from django.http import HttpResponse
import requests


def send(request, complaint_type, msg_type, name, phone_num):
    complaint_type.replace("-", " ")
    return HttpResponse(f'Working {phone_num} {msg_type} {name} {complaint_type}')
    #  api_key = '292a8d1f-295e-11e9-9ee8-0200cd936042'
    # if(msg_type == 2):
    #     template_name = 'Complaint Registration'
        # return redirect('home')
    # elif(msg_type == 3):
    #     template_name = 'Complaint Viewed'
        # return redirect('complaints:single', pk=pk)
    # elif(msg_type == 4):
    #     template_name = 'Complaint Comment'
    #     return redirect('complaints:single', pk=complaint.pk)
    # link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey={api_key}&to={phone_num}&from=ECIWEB&templatename={template_name}&var1={name}&var2={complaint_type}'
    # requests.get(link)
    

    



    


