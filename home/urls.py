
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    path("",views.index, name='home'),
    path("profile",views.profile, name='profile'),
    path("<int:id>/edi",views.edit_pro, name='edit_pro'),
    path("blog",views.blog, name='blog'),
    path("blog_details",views.blog_details, name='blog_details'),
    path("delete_blog",views.delete_blog, name='delete_blog'),
    path("blog_form",views.blog_form, name='blog_form'),
    path("comment",views.comment, name='comment'),
    path("delete_comment",views.delete_comment, name='delete_comment'),
    path("login",views.login, name='login'),
    path("logout",views.logout, name='logout'),
    path("signup",views.signup, name='signup'),
    path("profile",views.profile, name='profile'),
    path("event",views.event, name='event'),
    path("event_gelary",views.event_gelary, name='event_gelary'),
    path("tour_form",views.tour_form, name='tour_form'),
    path("tour_details",views.tour_details, name='tour_details'),

   

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
