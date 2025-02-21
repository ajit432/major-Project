from django.shortcuts import render
from student.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login , logout
# Create your views here.

def student_home(request):
    student_user_name= request.session.get("student_username")
    if student_user_name:
        Student_Object =  User.objects.get(username =student_user_name )
        Student_Profile_Object = StudentProfile.objects.get(username = Student_Object)
        d={'Student_Profile_Object':Student_Profile_Object,'Student_Object':Student_Object}
        return render(request,'students/student_home.html',d)
    return render(request,'students/student_home.html')


def student_register(request):
    ESUFO= StudentUserForm()
    ESPFO= StudentProfileForm()
    d={'ESUFO':ESUFO,'ESPFO':ESPFO}
    if request.method =="POST" and request.FILES:
        SUFDO=StudentUserForm(request.POST)
        SPFDO=StudentProfileForm(request.POST,request.FILES)
        if SUFDO.is_valid() and SPFDO.is_valid():
            pw = SUFDO.cleaned_data.get('password')
            MSUFDO = SUFDO.save(commit=False)
            MSUFDO.set_password(pw)
            MSUFDO.save()

            MSPFDO =SPFDO.save(commit=False)
            MSPFDO.username = MSUFDO
            MSPFDO.save()

            email = SUFDO.cleaned_data.get('email')
            massage = f"Welcome to {MSUFDO.first_name} ,\n Thank You for Register To our Website form phone number is {MSPFDO.phone} \n \t Thnak You "
            send_mail(
                "Successfull Registraions Done",
                massage,
                "ajitkumarbehera432@gmail.com",
                [email],
                fail_silently=False
            )
            # return HttpResponse("Student Registration Done ...................")
            return HttpResponseRedirect(reverse('student_login'))
    return render(request,'students/student_register.html',d)


def student_login(request):
    if request.method =="POST":
        student_username = request.POST.get('username')
        student_password = request.POST.get('password')
        AUO = authenticate(username=student_username, password = student_password)
        if AUO :
            request.session['student_username'] = student_username
            login(request,AUO)
            # return HttpResponse("Login Done ...................")
            return HttpResponseRedirect(reverse('student_home'))
        return HttpResponse('Invalid Credential')
    return render(request,'students/student_login.html')

 
# user decorator  check user login or not , if user not login it redirct to login page
def login_required(func):
    def inner(request, *args, **kwargs):
        un = request.session.get('student_username')
        if un :
            return func(request,*args,  **kwargs)
        return HttpResponseRedirect(reverse('student_login'))
    return inner

@login_required
def student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('student_home'))
 



# dispaly Student Profile 
@login_required
def student_profile_display(request):
    student_user_name= request.session.get("student_username")
    if student_user_name:
        Student_Object =  User.objects.get(username =student_user_name )
        Student_Profile_Object = StudentProfile.objects.get(username = Student_Object)
        d={'Student_Profile_Object':Student_Profile_Object,'Student_Object':Student_Object}
        return render(request,'students/student_profile_display.html',d)
    return HttpResponseRedirect(reverse('student_login'))


@login_required
def myratings(request):
    student_username =request.session.get("student_username")
    SO = User.objects.get(username = student_username)
    Student_Profile_Object=StudentProfile.objects.get(username = SO)
    d={'SO':SO,'Student_Profile_Object':Student_Profile_Object}
    return render(request,'students/myratings.html',d)