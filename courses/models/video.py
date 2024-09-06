from django.db import models
from courses.models import Course

class Video(models.Model):
    serial_number = models.IntegerField(null=False)
    title = models.CharField(max_length=100 , null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    video = models.FileField(upload_to="videos/")
    is_preview = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title