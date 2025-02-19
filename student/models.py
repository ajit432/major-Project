from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentProfile(models.Model):
    courses =[
        ('Python full stack','Python full stack'),
        ('Java full stack','Java full stack'),
        ('Mern full stack','Mern full stack'),
        ('Testing with Python','Testing with Python')
    ]
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    course = models.CharField( max_length=50, choices=courses , default='Python full stack')
    profile_pic = models.ImageField(upload_to='student_profiles', height_field=None, width_field=None, max_length=None) 
    resume = models.FileField(upload_to="student_resumes", max_length=100)

    def __str__(self):
        return self.username.username 
    

