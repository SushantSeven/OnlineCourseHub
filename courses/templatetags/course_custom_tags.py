from django import template
import math

from courses.models import Usercourse, Course
register = template.Library()

@register.simple_tag
def cal_sellprice(price , discount):
    if discount is None or discount is 0:
        return price
    
    sellprice = price
    sellprice = price - (price * discount * 0.01)
    return math.ceil(sellprice)

@register.filter
def rupee(price):
    return f'₹{price}'

@register.simple_tag
def is_enrolled(request , course):
    user = None
    if not request.user.is_authenticated:
        return False
    user=request.user
    try:
        user_course = Usercourse.objects.get(user=user, course=course)
        return True
    except:
        return False
    

# test

@register.simple_tag
def free_course(request, course):
    if not request.user.is_authenticated:
        return False
    else:
        if course.price == 0:
            return True
        else:
            return False