from home.form import BlogForm
from django.shortcuts import render
from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render ,HttpResponse,redirect
from .models import *

from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
import datetime


from django.forms.widgets import NullBooleanSelect
from django.shortcuts import render ,HttpResponse,redirect
from .models import *

from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
import datetime


# Create your views here.
def index (request):
    data=Blog.objects.all()
    i=0
    a=[]
    for temp in data:
        if i>2:
            break
        a.append(temp)
            
   
  

    print("Hi I am From View")
    return render(request,'home.html',{'data':a[0]})

def profile (request):

    if request.user.is_authenticated:
        data=Profile.objects.all()
        data2=Blog.objects.all()
        data3=Event.objects.all()
        c=Comment.objects.all()
        a=[]
        b=[]
        
        for temp in data2:
            s=str(temp.username)
            if s==str(request.user.username):
                a.append(temp)
        print(a)
           
            
        for temp in data3:
            s=str(temp.username)
            if s==request.user.username:
                b.append(temp)     
            
        return render(request,'profile.html',{'data':data, 'a':a})
    else:
        return HttpResponse("Please Login First")

def blog (request):

   
    data=Blog.objects.all()

       
    return render(request,'blog.html', {'data':data})
def blog_form (request):
    if request.user.is_authenticated:       
        form=BlogForm()
        if request.method =='POST':
            form=BlogForm(request.POST,request.FILES)
            
            if form.is_valid():
                instance=form.save(commit=False)
                print("User")
                print(instance)
                instance.username=request.user.profile
                form.save()
               
            return redirect('blog')
        return render(request,'blog_form.html',{'form':form})
    else:
        return HttpResponse("Please Login First")
def delete_blog (request):
        if request.user.is_authenticated:
            target=request.POST.get('System')
            
            print("__________________________________________________________")
            print(target)
            data=Blog.objects.all()
            for temp in data:
                s=str(temp)
                if s==target:
                    temp.delete()
            return redirect('profile')
        else:
            return HttpResponse("Please Login First")
def blog_details (request):
    if request.user.is_authenticated:
        pk=request.POST.get('System2')
        
        data=Blog.objects.all()
        data2=Profile.objects.all()
        data3=Comment.objects.all()
        a=[]
        for temp in data:
            id=str(temp.id)

            if pk == id:
                for temp3 in data3:
                    c1=str(temp3.blog)
                    c2=str(temp)
                    if c1==c2:
                        a.append(temp3)
 
                for temp2 in data2:
                    s1=str(temp.username)
                    s2=str(temp2.user)
                    print(s1)
                    print(s2)
                    if s1==s2:
                
                
                        return render(request,'blog_details.html',{'temp':temp,'temp2':temp2,'a':a})
                
    else:
        return HttpResponse("Please Login First")


def comment (request):
        
        if request.user.is_authenticated:
            pk=request.POST.get('System2')
           
            cmt=request.POST.get('comment')
          
            data=Blog.objects.all()
            for temp in data:
                s=str(temp.id)
                if s==pk:
                    id2=temp
            blog=id2
            post=cmt
            user=request.user
            new_post=Comment(blog=blog, post=post, user=user)
            new_post.save()
         
            return redirect('blog')
        else:
            return HttpResponse("Please Login First") 
def delete_comment (request):
        #if request.user.is_authenticated:
            target=request.POST.get('Comment')
            print(target)
            data=Comment.objects.all()
            for temp in data:
                s=str(temp)
                if s==target:
                    temp.delete()
            return redirect('blog')
        #else:
         #   return HttpResponse("Please Login First")
def event(request):
    data=Event.objects.all()
    print(data)
    print("-------------------------------------------------------------------------")

    return render(request,'travle_list.html', {'data':data})
def event_gelary(request):
    data=EventImage.objects.all()

    return render(request,'event_gelary.html',{'data':data})

##Login Logout
def login (request):

    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        
        user=authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return render(request,'login.html')


    return render(request,'login.html')
def logout (request):
    if request.user.is_authenticated:
        auth.logout(request)
        return HttpResponse("You logout successfully")
    else:
        return HttpResponse("Please Login First")
def signup (request):
    if request.method == 'POST':
      form=UserCreationForm(request.POST)

      if form.is_valid():
          form.save()
          return redirect('login')
    else:
        form=UserCreationForm()
    return render (request,'singnup.html',{'form': form})
