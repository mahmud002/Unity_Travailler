from django.urls.base import resolve
from home.views import delete_blog
from django.http import request, response
from django.test import TestCase
from .models import *
from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render ,HttpResponse,redirect
from .models import *
from .views import *

from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User,auth
import datetime

from home import views



from django.test import TestCase, Client
from django.urls import reverse
import json

# Create your tests here.

class TestView(TestCase):
    def test_blog(self):
        url=reverse('blog')
        self.assertEquals(resolve(url).func, blog)
        
        response=self.client.get(reverse('blog'))
        self.assertTemplateUsed(response, 'blog.html')

    def test_template_login(self):
        
        response=self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')    


    def test_template_event(self):
        
        response=self.client.get(reverse('event'))
        self.assertTemplateUsed(response, 'travle_list.html')

    def test_template_event_gelary(self):
        
        response=self.client.get(reverse('event_gelary'))
        self.assertTemplateUsed(response, 'event_gelary.html')   
    
    
    def test_blog_model(self):
        self.blog=Blog.objects.create(title='title1')
        self.assertEquals(str(self.blog),'title1')

        
 
    
        





        
    
       

        
        




   



    
        

    


