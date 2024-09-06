from django.shortcuts import render, redirect
from courses.models import Course, Profile
from django.contrib.auth.models import User
from django.contrib import messages
def changepasswordPage(request, token):
        context = {}
        try:
            profile_obj = Profile.objects.filter(forgot_password_token = token).first()
            context = {'user_id' : profile_obj.user.id}

            print(profile_obj)

            if request.method == 'POST':
                   new_password = request.POST.get('new_password')
                   confirm_password = request.POST.get('confirm_password')
                   user_id = request.POST.get('user_id')

                   if user_id is None:
                          messages.error(request, "No User found")
                          return redirect('/change_password/{token}/')
                   if new_password != confirm_password:
                           messages.error(request, "Password doesnt match")
                           return redirect(f'/change_password/{token}/')
                   
                   user_obj = User.objects.get(id=user_id)
                   user_obj.set_password(new_password)
                   user_obj.save()
                   return redirect("login")
        
        except Exception as e:
                print(e)
                

        return render(request,template_name="courses/change_password.html", context=context)