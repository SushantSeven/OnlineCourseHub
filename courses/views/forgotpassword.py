from django.shortcuts import render, redirect
from courses.models import Course, Profile
from django.contrib.auth.models import User
from django.contrib import messages
from courses.helpers import send_forgot_password_mail
import uuid


def forgotpasswordPage(request):
    try:
        if request.method=="POST":

            username = request.POST.get('username')
            if not User.objects.filter(username = username).first():
                messages.error(request, 'No user found')
                return redirect("forgot_password")
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user = user_obj)
            profile_obj.forgot_password_token=token
            profile_obj.save()
            send_forgot_password_mail(user_obj, token)
            messages.success(request, 'Email sent')
            return redirect("forgot_password")
           
    except Exception as e:
        print(e)
    return render(request, 'courses/forgot_password.html')
