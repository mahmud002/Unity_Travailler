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

      
    def test_profile(self):
        client=Client()
        response = client.get(reverse('profile'))
        client.get('profile.html')

    def test_profile_url(self):
        url=reverse('profile')
        self.assertEquals(resolve(url).func, profile) 

    def test_blog_form(self):
        client=Client()
        response = client.get(reverse('blog_form'))
        client.get('blog_form.html')

    def test_blog_form_url(self):
        url=reverse('blog_form')
        self.assertEquals(resolve(url).func, blog_form) 

    def test_blog_details(self):
        client=Client()
        response = client.get(reverse('blog_details'))
        client.get('blog_details.html')

    def test_blog_details_url(self):
        url=reverse('blog_details')
        self.assertEquals(resolve(url).func, blog_details) 

    def test_image_delete_url(self):
        url=reverse('image_delete')
        self.assertEquals(resolve(url).func, image_delete) 
    def test_blog_details_url(self):
        url=reverse('tour_leave')
        self.assertEquals(resolve(url).func, tour_leave) 
    def test_blog_details_url(self):
        url=reverse('tour_join')
        self.assertEquals(resolve(url).func, tour_join) 








    def test_template_login(self):
        
        response=self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')


    def test_template_event(self):
        
        response=self.client.get(reverse('event'))
        self.assertTemplateUsed(response, 'travle_list.html')

    def test_event_url(self):
        url=reverse('event')
        self.assertEquals(resolve(url).func, event) 

    def test_template_event_gelary(self):
        
        response=self.client.get(reverse('event_gelary'))
        self.assertTemplateUsed(response, 'event_gelary.html')  

    def test_event_gelary_url(self):
        url=reverse('event_gelary')
        self.assertEquals(resolve(url).func, event_gelary) 
    
    
    def test_blog_model(self):
        self.blog=Blog.objects.create(title='title1')
        self.assertEquals(str(self.blog),'title1')

    def test_template_event(self):
        
        response=self.client.get(reverse('event'))
        self.assertTemplateUsed(response, 'travle_list.html')

    def test_event_url(self):
        url=reverse('event')
        self.assertEquals(resolve(url).func, event) 
        
    def test_Event_model(self):
        self.event=Event.objects.create(title='title1')
        self.assertEquals(str(self.event),'title1')

    
    def test_comment_model(self):
        self.comment=Comment.objects.create(post='hi')
        self.assertEquals(str(self.comment),'hi')



        #self.user=User.objects.create(username="mahmud", password="mahmud01")
        #self.profile=Profile.objects.create(user=self.user)
        

        #self.blog1=Blog.objects.create(
         #   username=self.profile,
          #  title='hello'
        #)


        
        
    def test_view_comment_post(self):
        self.client=Client()

        self.comment=Comment.objects.create(post='this_is_comment')
        self.list_url=('/comment')
        response=self.client.post(self.list_url,{
            'post':'this_is_comment'
        })

        self.assertEquals(response.status_code,200)
        self.assertEquals(str(self.comment.post),'this_is_comment')

        
        
    def test_view_comment_delete(self):
        self.client=Client()

        self.comment=Comment.objects.create(post='this_is_comment')
        self.list_url=('/delete_comment')

        response=self.client.delete(self.list_url,json.dumps({ 'id':1}))
        
        self.assertEquals(response.status_code,302)
        

    def test_view_blog_delete(self):
        self.client=Client()

        self.blog=Blog.objects.create(title='this_is_blog')
        self.list_url=('/delete_blog')

        response=self.client.delete(self.list_url,json.dumps({ 'id':1}))
        
        self.assertEquals(response.status_code,200)
        #self.assertEquals(self.comment.count(),0)

        
    def test_view_Blog_post(self):
        self.client=Client()

        self.blog=Blog.objects.create(post='this_is_blog')
        self.list_url=('/blog_form')
        response=self.client.post(self.list_url,{
            'post':'this_is_comment'
        })

        self.assertEquals(response.status_code,200)
        self.assertEquals(str(self.blog.post),'this_is_blog')
 

        
    




        
    
       

        
        




   



    
        

    


