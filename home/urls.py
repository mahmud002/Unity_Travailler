
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
    path("blog_details",views.blog_details, name='blog_details'),
    path("delete_blog",views.delete_blog, name='delete_blog'),
    path("comment",views.comment, name='comment'),
    path("login",views.login, name='login'),
    path("logout",views.logout, name='logout'),
    path("signup",views.signup, name='signup'),
    path("profile",views.profile, name='profile'),
    path("event",views.event, name='event')
   

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
