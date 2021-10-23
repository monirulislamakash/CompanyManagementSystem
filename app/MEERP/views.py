from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
from .form import *
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        confirm=UserStudent.objects.filter(Confirm=True)
        addmition=UserStudent.objects.filter(Confirm=False)
        print(len(confirm),len(addmition))
        sendvar={
            "confirm":int(len(confirm)),
            "addmition":int(len(addmition)),
        }
        return render(request,"index.html",sendvar)
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

def presingup(request):
    return render(request,"presingup.html")
    
def singup(request):
    prevalu=request.POST.get("presingup")
    if prevalu is not None:
        pfrom=Techer()
        sfrom=Student()
        sender={
            'prevalu':prevalu,
            'pfrom':pfrom,
            'sfrom':sfrom
        }
        return render(request,"singup.html",sender)
    return redirect(presingup)

def addusertecher(request):
    pfrom=Techer()
    if request.method=="POST":
        pfrom=Techer(request.POST,request.FILES)
        if pfrom.is_valid():
            pfrom.save()
            return render(request,"adduser.html",{'success':"user created successfully"})

def addstudent(request):
    sfrom=Student()
    if request.method=="POST":
        sfrom=Student(request.POST,request.FILES)
        if sfrom.is_valid():
            sfrom.save()
            return render(request,"adduser.html",{'success':"user created successfully"})
    return render(request,"adduser.html")
def profile(request):

    return render(request,"profile.html")

def adduser(request):
    email=request.POST.get("email")
    passw=request.POST.get("password")
    cpassw=request.POST.get("confirmpassword")
    if request.method=="POST":
        if passw==passw:
            try:
                user=User.objects.get(username=email)
                return render(request,"adduser.html",{'error':"User already exists"})  
            except User.DoesNotExist:
                user=User.objects.create_user(username=email,password=cpassw)
                return redirect(presingup)   
        else:
            return render(request,"adduser.html") 
    return render(request,"adduser.html")
def accounts(request):
    if request.method=="POST":
        usernamest=request.POST.get('user')
        amount=request.POST.get('amount')
        t = UserStudent.objects.get(COLLAGE_ID=usernamest)
        t.Due=int(t.Due)-int(amount)
        t.Paid=int(t.Paid)+int(amount)
        t.save()
    return render(request,'accounts.html')