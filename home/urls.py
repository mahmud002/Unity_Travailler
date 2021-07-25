
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    path("",views.index, name='home'),
    path("profile",views.profile, name='profile'),
    path("blog",views.blog, name='blog'),
    path("travle_list",views.travle_list, name='travle_list'),
    path("login",views.login, name='login'),
    path("logout",views.logout, name='logout'),
    path("signup",views.signup, name='signup'),
    path("profile",views.profile, name='profile')
   

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
