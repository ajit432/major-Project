from django.shortcuts import render
from manager.models import *
# Create your views here.
from django.contrib.auth import authenticate,login , logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from trainer.forms import *



def trainer_home(request):
    return render(request,'trainer/trainer_home.html')



def trainer_login(request):
    if request.method =="POST":
        trainer_username = request.POST.get('username')
        trainer_password = request.POST.get('password')
        AUO = authenticate(username=trainer_username, password = trainer_password)
        if AUO and AUO.is_staff:
            EO = EmployeeProfile.objects.get(username = AUO)
            if EO.role == 'Trainer':
                request.session['trainer_username'] = trainer_username
                login(request,AUO)
                # return HttpResponse(' Trainer is Login ........................................')
                return HttpResponseRedirect(reverse('trainer_home'))
            return HttpResponse('Its Trainer session not HR')
        return HttpResponse('Invalid Trainer Credential')
    return render(request,'trainer/trainer_login.html')


def trainer_login_requried(func):
    def inner(request, *args, **kwargs):
        trainer_username = request.session.get("trainer_username")
        if trainer_username:
            return func(request,*args,**kwargs)
        return HttpResponseRedirect(reverse('trainer_login'))
    return inner


@trainer_login_requried
def trainer_logout(request):
    logout(request)
    return render(request('trainer/trainer_home.html'))

@trainer_login_requried
def trainer_start_mock(request):
    EMRO = StudentMockForms()
    d={'EMRO':EMRO}
    if request.method == "POST":
        MRDO= StudentMockForms(request.POST)
        if MRDO.is_valid():
            trainer_user_name =request.session.get('trainer_username')
            TrainerObject = User.objects.get(username = trainer_user_name)
            MUMRDO= MRDO.save(commit=False)
            MUMRDO.conducted_by=TrainerObject
            MUMRDO.save()
            return HttpResponseRedirect(reverse('trainer_home'))
        return HttpResponse('Ivvalid MOCK data')
    return render(request,'trainer/trainer_start_mock.html',d)