from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os
# Create your models here.
class StudentProfile(models.Model):
    courses =[
        ('Python full stack','Python full stack'),
        ('Java full stack','Java full stack'),
        ('Mern full stack','Mern full stack'),
        ('Testing with Python','Testing with Python')
    ]
    # rename file name as use to validators
    def get_upload_path(self,filename):
        ext = filename.split(".")[-1]
        filename = f"{self.username.first_name}_{self.username.last_name}_resume.{ext}"
        return os.path.join("student_resumes",filename)
    
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    course = models.CharField( max_length=50, choices=courses , default='Python full stack')
    profile_pic = models.ImageField(upload_to='student_profiles', height_field=None, width_field=None, max_length=None) 
    # resume = models.FileField(upload_to="student_resumes", max_length=100)
    resume = models.FileField(upload_to=get_upload_path, validators=[FileExtensionValidator(['pdf','docx'])])

    def __str__(self):
        return self.username.username 
    

