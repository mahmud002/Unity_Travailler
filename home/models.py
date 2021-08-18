from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User,auth

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="home/images", default="",null=True, blank=True)
    address = models.TextField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return "%s" % (self.user)



class Blog(models.Model):
   
    username=models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    title=models.TextField(max_length=30, blank=True)
    intro=models.TextField(max_length=100, blank=True)
    post=models.TextField(max_length=2000, blank=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="home/images", default="",null=True, blank=True)

class Comment(models.Model):
   
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)
    post=models.TextField(max_length=200, blank=True)
    pub_date=models.DateTimeField(auto_now_add=True)


class Event(models.Model):
   
    username=models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    title=models.TextField(max_length=30, blank=True)
    intro=models.TextField(max_length=100, blank=True)
    post=models.TextField(max_length=2000, blank=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="home/images", default="",null=True, blank=True)