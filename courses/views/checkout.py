from django.shortcuts import render , redirect
from courses.models import Course , Video, Payment, Usercourse, CouponCode
from django.shortcuts import HttpResponse

# razorpay implementation
from onlinecourse.settings import *
from time import time
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }

@login_required(login_url='/login')
def checkout(request, slug):
    course = Course.objects.get(slug = slug)
  
    # if not request.user.is_authenticated:
    #     return redirect("login")
    user = request.user
    action = request.GET.get('action')
    couponcode = request.GET.get('couponcode')
    coupon_code_message = None
    coupon = None
    order = None
    payment = None
    error=None
    amount = 0
    try:
        user_course = Usercourse.objects.get(user=user, course=course)
        error="You are Already Enrolled to this Course"
    except:
        pass
    if error is None: 
        amount = int((course.price - (course.price * course.discount * 0.01)) * 100)
     # if amount is zero directly save the enrollment object
    if amount == 0:
            usercourse = Usercourse(user=user, course = course)
            usercourse.save()
            return redirect("my-courses")
    if couponcode:
        try:
            coupon =  CouponCode.objects.get(course=course, code = couponcode)
            amount= course.price-(course.price * coupon.discount *0.01)
            amount = int(amount)*100
        except:
            coupon_code_message="Invalid coupon code"
            print("invalid coupon")

    if action == "create_payment":
    
            currency = "INR"
            notes = {
                "email" : user.email ,
                "name" : f'{user.first_name}{user.last_name}'
            }
            receipt = f"Online Course Hub_{int(time())}"
            order = client.order.create({'receipt': receipt, 'notes': notes, 'amount': amount, 'currency' : currency})
        
            payment = Payment()
            payment.user = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()
    
    
    context = {
        "course" : course ,
        "order" : order,
        "payment" : payment,
        "user" : user,
        "error" : error,
        "coupon":coupon,
        "coupon_code_message":coupon_code_message
    }
    return render(request,template_name="courses/check_out.html", context=context)

@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        context ={}
        try:
             client.utility.verify_payment_signature(data)
             razorpay_order_id = data['razorpay_order_id']
             razorpay_payment_id = data['razorpay_payment_id']

             payment = Payment.objects.get(order_id = razorpay_order_id)
             payment.payment_id = razorpay_payment_id
             payment.status = True
             
             usercourse = Usercourse(user=payment.user, course = payment.course)
             usercourse.save()

             payment.user_course = usercourse
             payment.save()
             return redirect("my-courses")
             
        except:
            return HttpResponse("Invalid payment details")