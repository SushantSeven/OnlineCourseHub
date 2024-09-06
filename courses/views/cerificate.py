# # myapp/views.py
from django.http import JsonResponse
from courses.models import Course , Video, Usercourse
from django.shortcuts import render , redirect,HttpResponse


import cv2

def run_python_script(request):
    if request.user.is_authenticated is False:
            return redirect("login")
    else:
            user = request.user
            full_name = user.get_full_name()
    
            template = cv2.imread('Blank-Award-Certificate.jpg')
            cv2.putText(template, full_name, (260,297), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,255), 1, cv2.LINE_AA)
            cv2.imwrite(f'D:\games\{full_name}.jpg', template)
            print('processing Certificate ')
            return HttpResponse("<h1>certifiate printed successfully<h2>")
    