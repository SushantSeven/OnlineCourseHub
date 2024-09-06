from django.contrib import admin
from courses.models import Course, Learning, Prerequisite, Tag, Video , Usercourse, Payment, CouponCode
from django.utils.html import format_html
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class VideoAdmin(admin.StackedInline):
    model = Video

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin]  
    list_display = ["name","get_price","get_discount", "active"]
    list_filter = ("discount", 'active')
    def get_discount(self,course):
        return f"{course.discount} %"
    
    def get_price(self,course):
        return f"₹ {course.price}"
    get_discount.short_description = "Discount"
    get_price.short_description = "Price"

class PaymentAdmin(admin.ModelAdmin):
    model=Payment
    list_display = ['order_id','user', 'course', 'status']
    list_filter = ('status', 'course')

    def get_user(self, payment):
        return format_html(f"<a href='/login'>{payment.user}</a>")

admin.site.register(Course, CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Usercourse)
admin.site.register(CouponCode)

