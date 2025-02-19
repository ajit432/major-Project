from django.shortcuts import render
from manager.models import *
# Create your views here.
from django.contrib.auth import authenticate,login , logout
from django.http import HttpResponse, HttpResponseRedirect



def hr_home(request):
    return render(request,'hr/hr_home.html')



def hr_login(request):
    if request.method =="POST":
        hr_username = request.POST.get('username')
        hr_password = request.POST.get('password')
        AUO = authenticate(username=hr_username, password = hr_password)
        if AUO and AUO.is_staff:
            request.session['hrusername'] = hr_username
            login(request,AUO)
            return HttpResponse(' HR is Login ..............................................')
            # return HttpResponseRedirect(reversed('hr_home'))
        return HttpResponse('Invalid Hr Credential')
    return render(request,'hr/hr_login.html')




def hr_logout(request):
    logout(request)
    return render(request,'hr/hr_home.html')
     