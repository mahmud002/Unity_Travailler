from home.form import BlogForm, EventImageForm, ProfileForm, TourForm
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
    data2=Profile.objects.all()
    i=0
    a=[]
    for temp in data:
        if i>2:
            break
        a.append(temp)
            
   


    print("Hi I am From View with merge")
    return render(request,'home.html',{'data':a[0],'data2':data2})

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
def edit_pro (request,id):
        if request.user.is_authenticated:
            
            if request.method=='POST':
                pi=Profile.objects.get(pk=id)

                fm=ProfileForm(request.POST, request.FILES,instance=pi)
                if fm.is_valid:
                    fm.save()
                    return redirect('profile')

            else:
                pi=Profile.objects.get(pk=id)
                
                fm=ProfileForm(instance=pi)

            return render(request,'profile_form.html',{'form':fm})

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

def tour_details (request):
    if request.user.is_authenticated:
        pk=request.POST.get('System2')
        
        data=Event.objects.all()
        data2=Profile.objects.all()
        data3=Member.objects.all()
     
        a=[]
        b=[]
        for temp in data3:
            id= (str)(temp.event.id)
            if id==pk:
                b.append(temp)
            
        for temp in data:
           
            id=str(temp.id)

            if pk == id:
 
 
                for temp2 in data2:
                    s1=str(temp.username)
                    s2=str(temp2.user)
                    print(s1)
                    print(s2)
                    if s1==s2:
                
                
                        return render(request,'tour_details.html',{'temp':temp,'temp2':temp2,'temp3':b})
                
    else:
        return HttpResponse("Please Login First")


def comment (request):
        
        if request.user.is_authenticated:
            pk=request.POST.get('System2')
           
            cmt=request.POST.get('comment')
            print("Hello World")
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
    data2=Member.objects.all()
    a=[]
    b=[]
    c=[]
    #all Event
    for temp in data2:
        s=(str)(temp.user)
        s1=(request.user.username)
        if(s==s1):
            b.append(str(temp.event.id))
    #my event
    for temp in data:
        s=str(temp.username)
        if  str(temp.id) in b:
            a.append(temp)
    for temp in data:
        s=str(temp.username)
        if s==str(request.user.username) :
            c.append(temp)
  

    return render(request,'travle_list.html', {'data':a,'data2':data,'data3':c})

def event_gelary(request):
    pk=request.POST.get('System2')
    a=[]
    data=EventImage.objects.all()
    print(type(pk))
    z=str(pk)
    
    for temp in data:
        
        if pk==(str)(temp.gelary.id):
            a.append(temp)
    p=str(pk)
    return render(request,'event_gelary.html',{'data':a,'pk':p})

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

def tour_form (request):

    if request.user.is_authenticated:       
        form=TourForm()
        if request.method =='POST':
            form=TourForm(request.POST,request.FILES)
            
            if form.is_valid():
                instance=form.save(commit=False)
                print("User")
                print(instance)
                instance.username=request.user.profile
                form.save()
               
            return redirect('event')
        return render(request,'tour_form.html',{'form':form})
    else:
        return HttpResponse("Please Login First")
def tour_join (request):

    if request.user.is_authenticated:       
       
        if request.method =='POST':
            pk=request.POST.get('System5')
            data=Event.objects.all()
            
            for a in data:
                if (str)(a.id)==(str)(pk):
                    temp=a
                    reg = Member(event=temp,user=request.user.profile)
                    print(reg)
                    reg.save()
           
            

            return redirect('event')
        
    else:
        return HttpResponse("Please Login First")
def tour_leave (request):

    if request.user.is_authenticated:       
       
        if request.method =='POST':
            pk=request.POST.get('System6')

            data=Member.objects.all()

            for temp in data:
                if (str)(temp.event.id)==(str)(pk):
                    temp.delete()
                    
            
            
            

            return redirect('event')
        
    else:
        return HttpResponse("Please Login First")


def tour_delete (request):

    if request.user.is_authenticated:       
       
        if request.method =='POST':
            pk=request.POST.get('System10')

            data=Event.objects.all()

            for temp in data:
                if (str)(temp.id)==(str)(pk):
                    temp.delete()
                    
            
            
            

            return redirect('event')
        
    else:
        return HttpResponse("Please Login First")


def blog_detail_view( request, pk):
    p=str(pk)
    data=Event.objects.all()
    for temp in data:
        if str(temp.id)==p:
            print("this"+p)
            print(temp)
            form=EventImageForm()
            if request.method =='POST':
                form=EventImageForm(request.POST,request.FILES)
            
                if form.is_valid():
                    instance=form.save(commit=False)
            
                    instance.gelary=temp
                    form.save()
               
                    return redirect('event')
            return render(request,'image_form.html',{'form':form})


    return HttpResponse("Please Login First")


def image_delete (request):
        if request.user.is_authenticated:
            target=request.POST.get('Systemform8')
            
           
            print(target)
            print("_______________________________________________")
            data=EventImage.objects.all()
            for temp in data:
                s=str(temp)
                if s==target:
                    temp.delete()
            return redirect('event')
        else:
            return HttpResponse("Please Login First")


def blog_edit_view2( request, pk):
    p=str(pk)
    print(p+"________________________________________________________________")
    if request.method=='POST':
                pi=Blog.objects.get(pk=pk)

                fm=BlogForm(request.POST, request.FILES,instance=pi)
                if fm.is_valid:
                    fm.save()
                    return redirect('profile')

    else:
                pi=Blog.objects.get(pk=pk)
                
                fm=BlogForm(instance=pi)

    return render(request,'blog_form.html',{'form':fm})



def blog_edit_view3( request, pk):
    p=str(pk)
    print(p+"________________________________________________________________")
    if request.method=='POST':
                pi=Event.objects.get(pk=pk)

                fm=TourForm(request.POST, request.FILES,instance=pi)
                if fm.is_valid:
                    fm.save()
                    return redirect('profile')

    else:
                pi=Event.objects.get(pk=pk)
                
                fm=TourForm(instance=pi)

    return render(request,'tour_form.html',{'form':fm})

