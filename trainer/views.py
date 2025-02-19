from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate,login , logout
from django.http import HttpResponse, HttpResponseRedirect



def trainer_home(request):
    return render(request,'trainer/trainer_home.html')



def trainer_login(request):
    if request.method =="POST":
        trainer_username = request.POST.get('username')
        trainer_password = request.POST.get('password')
        AUO = authenticate(username=trainer_username, password = trainer_password)
        if AUO and AUO.is_staff:
            request.session['trainerusername'] = trainer_username
            login(request,AUO)
            return HttpResponse(' Trainer is Login ........................................')
        return HttpResponse('Invalid Trainer Credential')
    return render(request,'trainer/trainer_login.html')




def trainer_logout(request):
    logout(request)
    return render(request('trainer/trainer_home.html'))