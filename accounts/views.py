from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# from django import forms

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        user_name=request.POST['username']
        email=request.POST['firstname']
        password1=request.POST['psw']
        password2=request.POST['psw-repeat']
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Emailid Already Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                # messages.info(request,"User Registered")
                print("USER registerd")
                return redirect('/')
        else:
            messages.info(request,"Passsword Doesn't match")
            return redirect('register')
            # raise forms.ValidationError("Passwords don't match")
    else:
        
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')