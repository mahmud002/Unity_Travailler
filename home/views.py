from django.shortcuts import render
from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render ,HttpResponse,redirect
from .models import *

from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
import datetime


# Create your views here.
def index (request):
    print("Hi I am From View")
    return render(request,'home.html')

def profile (request):

    if request.user.is_authenticated:
        data=Profile.objects.all()
 
            
        return render(request,'profile.html',{'data':data})
    else:
        return HttpResponse("Please Login First")

def blog (request):

    print("Hi I am From View Blog")


    return render(request,'blog.html')
def travle_list (request):

    print("Hi I am From View Blog")


    return render(request,'travle_list.html')


##Login Logout
def login (request):

    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        
        user=authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return render(request,'login.html')


    return render(request,'login.html')
def logout (request):
    if request.user.is_authenticated:
        auth.logout(request)
        return HttpResponse("You logout successfully")
    else:
        return HttpResponse("Please Login First")
def signup (request):
    if request.method == 'POST':
      form=UserCreationForm(request.POST)

      if form.is_valid():
          form.save()
          return redirect('login')
    else:
        form=UserCreationForm()
    return render (request,'singnup.html',{'form': form})
