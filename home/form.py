from django.forms import ModelForm
from .models import *




class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields= '__all__'
        exclude=['username']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields= '__all__'
        exclude=['user']

class TourForm(ModelForm):
    class Meta:
        model = Event
        fields= '__all__'
        exclude=['username']