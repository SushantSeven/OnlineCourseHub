from django.shortcuts import render
from courses.models import Course


def hightolow(request):
        courses = Course.objects.filter().order_by('price').reverse()
        return render(request,template_name="courses/home.html",context={ "courses":courses})