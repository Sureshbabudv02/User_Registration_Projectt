from django.shortcuts import render

from app.models import *
# Create your views here.
from app.forms import *
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def registration(request):
    UFO = UserForm()
    PFO = ProfileForm()
    d = {'UFO':UFO,'PFO':PFO}
    if request.method =='POST' and request.FILES:
       UFD = UserForm(request.POST)
       PFD = ProfileForm(request.POST,request.FILES)
       if UFD.is_valid() and PFD.is_valid():
           MUFDO = UFD.save(commit=False)
           password = UFD.cleaned_data['password']
           MUFDO.set_password(password)
           MUFDO.save()
           MPFDO = PFD.save(commit=False)
           MPFDO.username = MUFDO
           MPFDO.save()
           return HttpResponse('<h1>Registered Successfully')
       else:
           return HttpResponse("Invalid")
    return render(request,'registration.html',d)