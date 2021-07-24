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