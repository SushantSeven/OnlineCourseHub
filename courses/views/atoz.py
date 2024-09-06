from django.shortcuts import render
from courses.models import Course


def filteratoz(request):
        courses = Course.objects.filter().order_by('name')
        return render(request,template_name="courses/home.html",context={ "courses":courses})