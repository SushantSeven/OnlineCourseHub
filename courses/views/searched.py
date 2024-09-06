from django.shortcuts import render
from courses.models import Course

def searchedPage(request):
    if request.method == "POST":
        searchfield = request.POST['searchfield']
        searched_course = Course.objects.filter(name__contains = searchfield)
        return render(request,template_name="courses/searched.html", context={'searchfield' : searchfield , 'searched_course': searched_course})
    else:
         return render(request,template_name="courses/searched.html")