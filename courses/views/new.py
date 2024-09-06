from django.shortcuts import render
def newpage(request):
    
    return render(request,template_name="courses/new.html")