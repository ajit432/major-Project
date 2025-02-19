from django.shortcuts import render
from manager.forms import *
import random
import string
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login , logout
# Create your views here.
def manager_home(request):
    return render(request,'manager/manager_home.html')


def add_employee(request):
    EEUFO = EmployeeUserForm()
    EEPFO = EmployeeProfileForm()
    d={'EEUFO':EEUFO,'EEPFO':EEPFO}

    if request.method == "POST":
        EUFDO= EmployeeUserForm(request.POST)
        EPFDO = EmployeeProfileForm(request.POST)

        if EUFDO.is_valid() and EPFDO.is_valid():
            un= f"{EUFDO.cleaned_data.get('first_name')}{EPFDO.cleaned_data.get('phone')[-4:]}"
            pw = ''.join([random.choice(string.punctuation) for i in range(1,6)])
            email = EUFDO.cleaned_data.get('email')

            MEUFDO = EUFDO.save(commit=False)
            MEUFDO.username=un
            MEUFDO.set_password(pw)
            MEUFDO.is_staff=True
            MEUFDO.save()

            MEPFDO =EPFDO.save(commit=False)
            MEPFDO.username =MEUFDO
            
            
            role =EPFDO.cleaned_data.get('role')
            # massage =f"Your Username Is :{un} \n Your Password Is : {pw} \n your designation is{{EPFDO.role}} \nThank Your Support"
            massage =f"Your Username Is :{un} \n Your Password Is : {pw} \n your designation is : {role} \nThank Your Support"
            send_mail(
                'Username And Password For Employeee',
                massage,
                'ajitkumarbehera432@gmail.com',
                [email],
                fail_silently=False
            )
            MEPFDO.save()
            print(f"your Username Is {un}")
            print(f"your password Is {pw}")
            return HttpResponseRedirect(reverse('manager_home'))
        return HttpResponse('Invalid Data Of Employeeeeeeeeeeeeeee')
    return render(request,'manager/add_employee.html',d)





def manager_login(request):
    if request.method =="POST":
        manager_username = request.POST.get('username')
        manager_password = request.POST.get('password')
        AUO = authenticate(username=manager_username, password = manager_password)
        if AUO  and AUO.is_superuser:
            request.session['managerusername'] = manager_username
            login(request,AUO)
            # return HttpResponse(' Mnager  Credential is Login')
            return HttpResponseRedirect(reverse('manager_home'))
        return HttpResponse('Invalid Credential')
    return render(request,'manager/manager_login.html')



def manager_login_required(func):
    def inner(request, *args, **kwargs):
        un = request.session.get('managerusername')
        if un :
            return func(request,*args,  **kwargs)
        return HttpResponseRedirect(reverse('manager_home'))
    return inner


@manager_login_required
def manager_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('manager_home'))