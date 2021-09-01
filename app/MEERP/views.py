from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request,"index.html")
    return redirect(login)

def login(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    if request.method=="POST":
       user=auth.authenticate(username=email,password=passw)
       if user is not None:
            auth.login(request,user)
            return redirect(index) 
       else:
            return render(request,"login.html",{'error':"Invalide User Password"})
    return render(request,"login.html") 
def logout(request):
    auth.logout(request)
    return redirect(index)
def singup(request):
    prevalu=request.POST.get("presingup")
    print(prevalu)
    return render(request,"singup.html")