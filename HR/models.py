from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student_Ratings_Data(models.Model):
    subjects=[
        ('Pyhton',"Pyhton"),
        ('java',"java"),
        ('Web_Tech',"Web_Tech"),
        ('SQL',"SQL"),
        ('Django',"Django"),
        ('JS',"JS"),
        ('RESTAPI',"RESTAPI"),
    ]

    marks_ratings =[
        ("*","*"),
        ("1","1"),
        ("2","2"),
        ("3","3"),
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students")
    subject = models.CharField( max_length=50,choices=subjects)
    communication = models.CharField( max_length=50, choices=marks_ratings , default=1 )
    technical = models.CharField( max_length=50, choices=marks_ratings, default=1)
    programming = models.CharField( max_length=50, choices=marks_ratings, default=1 )
    remarks =models.CharField( max_length=550)
    conducted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    conducted_on=models.DateField( auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.student.username
