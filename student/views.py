from django.shortcuts import render
from student.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login , logout
# Create your views here.

def student_home(request):
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
            return HttpResponse("Student Registration Done ...................")
    return render(request,'students/student_register.html',d)


def student_login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        AUO = authenticate(username=username, password = password)
        if AUO :
            request.session['username'] = username
            login(request,AUO)
            # return HttpResponse("Login Done ...................")
            return HttpResponseRedirect(reverse('student_home'))
        return HttpResponse('Invalid Credential')
    return render(request,'students/student_login.html')

 
# user decorator  check user login or not , if user not login it redirct to login page
def login_required(func):
    def inner(request, *args, **kwargs):
        un = request.session.get('username')
        if un :
            return func(request,*args,  **kwargs)
        return HttpResponseRedirect(reverse('student_login'))
    return inner

@login_required
def student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('student_home'))
 