from django.http import request
from django.test import TestCase
from .models import *
from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render ,HttpResponse,redirect
from .models import *

from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
import datetime


# Create your tests here.

class testBlog(TestCase):
    def setUp(self):
        User.objects.create(username="mahmud", password="mahmud01")
        User.objects.create(username="nishi", password="nishi01")
        Profile.objects.create(user=User.objects.get( username="mahmud"),address="Rampura",phone="11111")
        Profile.objects.create(user=User.objects.get( username="nishi"),address="Mirpur",phone="22222")

        Blog.objects.create(username=Profile.objects.get(user="1"),title="Title1",intro="Intro1",post="Post1",pub_date=10-10-10)
   

      


        
    


    



    def testUser(self):
        print("User Testing...................")
        obj1=User.objects.get( username="mahmud")
        self.assertEqual(obj1.username,"mahmud")
        self.assertEqual(obj1.password,"mahmud01")

        obj2=User.objects.get( username="nishi")
        self.assertEqual(obj2.password,"nishi01")


       


    def testProfile(self):
        print("Profile Testing...................")
        obj2=Profile.objects.all()
        obj3=Profile.objects.get(user="1")
        self.assertEqual(obj3.address,"Rampura")
        self.assertEqual(obj3.phone,"11111")
        obj4=Profile.objects.get(user="2")
        self.assertEqual(obj4.address,"Mirpur")
        self.assertEqual(obj4.phone,"22222")
        

    def testBlog(self):
        print("Blog Testing...................")
        obj3=Blog.objects.get(id="1")
        self.assertEqual(obj3.title,"Title1")
        self.assertEqual(obj3.intro,"Intro1")
        self.assertEqual(obj3.post,"Post1")
   



    
        

    


