from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse


# Create your views here.

def login(request):
    if request.method=="POST":
        user = auth.authenticate(username=request.POST['input_user_name'],password=request.POST['input_password'])
        if user is not None:
            auth.login(request,user)
            return redirect('product_home')
        else:
            return render(request,'accounts/login.html',{'error':'Username or passowrd is not correct'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('product_home')
    # if request.method=="POST":
    #     auth.logout(request)
    #     return redirect('product_home')
    # else:
    #     return HttpResponse('welcome')

def signup(request):
    if request.method=="POST":
        if request.POST['input_password1']==request.POST['input_password2']:
            try:
                user = User.objects.get(username=request.POST['input_user_name'])
                return render(request,'accounts/signup.html',{'error':'UserName already exists! '})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['input_user_name'],password=request.POST['input_password1'])
                # auth.login(request,user)
                return redirect('product_home')
        else:
            return render(request,'accounts/signup.html',{'error':'Password should match '})
    else:
        return render(request,'accounts/signup.html')
