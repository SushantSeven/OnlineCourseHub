from django.shortcuts import render
from courses.models import Course


def lowtohigh(request):
        courses = Course.objects.filter().order_by('price')
        return render(request,template_name="courses/home.html",context={ "courses":courses})