
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("profile",views.profile, name='profile'),
    path("blog",views.blog, name='blog'),
    path("travle_list",views.travle_list, name='travle_list'),
    path("login",views.login, name='login'),
    path("logout",views.logout, name='logout'),
    path("signup",views.signup, name='signup')
   

    
]
