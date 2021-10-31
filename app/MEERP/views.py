from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
from .form import *
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            confirm=UserStudent.objects.filter(Confirm=True)
            addmition=UserStudent.objects.filter(Confirm=False)
            fieldname=UserStudent.objects.all()
            Dep=Department.objects.all()
            ses=Session.objects.all()
            Parsonal=['Student_Name','MOBILE_NO_STUDENT','FATHERS_NAME','MOTHERS_NAME',
            'FATHER_MOBILE','MOTHERS_MOBILE','ADDRESS_PARMANENT','ADDRESS_LOCAL',
            'RELIGION','GENDER','District','Upazila_OR_Thana','Gurdian_Name','Gurdian_Relation','Father_NID',
            'Mother_NID','Student_NID_or_Birth_Crtificate']
            sendvar={
                "confirm":int(len(confirm)),
                "addmition":int(len(addmition)),
                'fildname':fieldname,
                'Department':Dep,
                'Session':ses,
                'Parsonal':Parsonal
            }
            return render(request,"index.html",sendvar)
        elif request.user.userteacher.DNID == "Teacher":
            return render(request,"index.html",{"Teacher":"Teacher"})
        elif request.user.userstudent.DNID == "student":
            return render(request,"index.html",{"student":"student"})
    return redirect(login)
def studentsearchpro(request):
    Student_Name=request.POST.get("studentname")
    MOBILE_NO_STUDENT=request.POST.get("student_phone")
    FATHERS_NAME=request.POST.get("fathername")
    MOTHERS_NAME=request.POST.get("mother_name")
    FATHER_MOBILE=request.POST.get("father_phone")
    MOTHERS_MOBILE=request.POST.get("mother_phone")
    if Student_Name=='on':
        var=UserStudent.objects.get(COLLAGE_ID=17130)
        sendvar={
            'var':var
        }
        return render(request,"studentsearchpro.html",{'studentname':'studentname'},sendvar)
    if MOBILE_NO_STUDENT=='on':
        var=UserStudent.objects.get(COLLAGE_ID=17130)
        sendvar={
            'var':var
        }
        return render(request,"studentsearchpro.html",{'studentphone':'studentphone'},sendvar)
    if FATHERS_NAME=='on':
        var=UserStudent.objects.get(COLLAGE_ID=17130)
        sendvar={
            'var':var
        }
        return render(request,"studentsearchpro.html",{'fathername':'fathername'},sendvar)
    if MOTHERS_NAME=='on':
        var=UserStudent.objects.get(COLLAGE_ID=17130)
        sendvar={
            'var':var
        }
        return render(request,"studentsearchpro.html",{'fatherphone':'fatherphone'},sendvar)
    if FATHER_MOBILE=='on':
        var=UserStudent.objects.get(COLLAGE_ID=17130)
        sendvar={
            'var':var
        }
        return render(request,"studentsearchpro.html",{'mothername':'mothername'},sendvar)
    if MOTHERS_MOBILE=='on':
        var=UserStudent.objects.get(COLLAGE_ID=17130)
        sendvar={
            'var':var
        }
        return render(request,"studentsearchpro.html",{'motherphone':'motherphone'},sendvar)
    '''ADDRESS_PARMANENT=request.POST.get("")
    ADDRESS_LOCAL=request.POST.get("")
    RELIGION=request.POST.get("")
    GENDER=request.POST.get("")
    District=request.POST.get("")
    Upazila_OR_Thana=request.POST.get("")
    Gurdian_Name=request.POST.get("")
    Gurdian_Relation=request.POST.get("")
    Father_NID=request.POST.get("")
    Mother_NID=request.POST.get("")
    Student_NID_or_Birth_Crtificate=request.POST.get("")'''
    return render(request,"studentsearchpro.html")

def studentsearch(request):
    if request.method=="POST":
        session=request.POST.get('Session')
        Group=request.POST.get('Group')
        Dep=request.POST.get('Department')
        Collageid=request.POST.get('Collageid')
        print(session,Group,Dep,Collageid)
        if session!="Select Session" and Group!="Select Group" and Dep!="Select Department":
            search=UserStudent.objects.raw('select * from userstudent where Session="'+session+'" and Section="'+Group+'" and Department="'+Dep+'"')
            print(search,"1")
            sendvar={
                'search':search
            }
            return render(request,"studentsearch.html",sendvar)
        elif session!="Select Session" and Dep!="Select Department":
            search=UserStudent.objects.filter(Session=session,Department=Dep)
            print(search,"2")
            sendvar={
                'search':search
            }
            return render(request,"studentsearch.html",sendvar)
        elif Group!="Select Group" and Dep!="Select Department":
            search=UserStudent.objects.filter(Section=Group,Department=Dep)
            print(search,"3")
            sendvar={
                'search':search
            }
            return render(request,"studentsearch.html",sendvar)


        elif Collageid!="4":
            search=UserStudent.objects.filter(COLLAGE_ID=Collageid)
            print(search,"")
            sendvar={
                'search':search
            }
            return render(request,"studentsearch.html",sendvar)
        elif Dep!="Select Department":
            search=UserStudent.objects.filter(Department=Dep)
            print(search,"5")
            sendvar={
                'search':search
            }
            return render(request,"studentsearch.html",sendvar)
    return render(request,"studentsearch.html")
        
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