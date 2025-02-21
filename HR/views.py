from django.shortcuts import render
from manager.models import *
# Create your views here.
from django.contrib.auth import authenticate,login , logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import *
from HR.models import *



def hr_home(request):
    return render(request,'hr/hr_home.html')



def hr_login(request):
    if request.method =="POST":
        hr_username = request.POST.get('username')
        hr_password = request.POST.get('password')
        AUO = authenticate(username=hr_username, password = hr_password)
        if AUO and AUO.is_staff:
            request.session['hrusername'] = hr_username
            UO=EmployeeProfile.objects.get(username=AUO)
            # print(UO.role)
            if UO.role == 'Hr':
                request.session['hr_username'] = hr_username
                login(request,AUO)
                # return HttpResponse(' HR is Login ..............................................')
                return HttpResponseRedirect(reverse('hr_home'))
            return HttpResponse('It Hr Session Not Trainer Session')
            # return HttpResponseRedirect(reversed('hr_home'))
        return HttpResponse('Invalid Hr Credential')
    return render(request,'hr/hr_login.html')

def hr_login_requried(func):
    def inner(request, *args, **kwargs):
        hr_username = request.session.get("hr_username")
        if hr_username:
            return func(request,*args,**kwargs)
        return HttpResponseRedirect(reverse('hr_login'))
    return inner

@hr_login_requried
def hr_logout(request):
    logout(request)
    return render(request,'hr/hr_home.html')
     


@hr_login_requried
def hr_set_mock(request):
    return render(request,'hr/hr_set_mock.html')




@hr_login_requried
def hr_show_student_ratings(request):
    ASRO=Student_Ratings_Data.objects.all()
    d={'ASRO':ASRO}
    return render(request,'hr/hr_show_student_ratings.html',d)
@hr_login_requried
def hr_show_student_ratings_indi(request,pk):
    ISRO=Student_Ratings_Data.objects.get(pk = pk)
    d={'ISRO':ISRO}
    return render(request,'hr/hr_show_student_ratings_indi.html',d)


