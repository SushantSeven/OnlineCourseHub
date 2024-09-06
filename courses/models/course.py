from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length = 50, null= False)
    slug = models.CharField(max_length = 50, null= False, unique=True)
    description = models.CharField(max_length=1000,null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to= "file/thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to="files/resources")
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class CourseProperty(models.Model):
    description = models.CharField(max_length=200 , null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract=True

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass
    
class Learning(CourseProperty):
    pass

class CouponCode(models.Model):
    code = models.CharField(max_length=6, null= True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name = "coupons")
    discount = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forgot_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username