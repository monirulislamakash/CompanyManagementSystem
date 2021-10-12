from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        alstudent=UserStudent.objects.all()
        sendvar={
            "confirm":int(len(alstudent))
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
        sender={
            'prevalu':prevalu,
        }
        return render(request,"singup.html",sender)
    return redirect(presingup)

def addusertecher(request):
    name=request.POST.get('name')
    designation=request.POST.get('designation')
    department=request.POST.get('department')
    date_of_join=request.POST.get('date_of_join')
    academic_qualification=request.POST.get('academic_qualification')
    experience=request.POST.get('experience')
    gender=request.POST.get('gender')
    Voter_id_smart=request.POST.get('Voter_id_smart')
    date_of_birth=request.POST.get('date_of_birth')
    address=request.POST.get('address')
    mobile_office=request.POST.get('mobile_office')
    mobile_personal=request.POST.get('mobile_personal')
    email=request.POST.get('email')
    password=request.POST.get('password')
    bio_data=request.POST.get('bio_data')
    image_1st=request.FILES['image_1st']
    image_2nd=request.FILES['image_2nd']
    scand_copy_of_nid=request.FILES['scand_copy_of_nid']
    all_of_your_certificate=request.FILES['all_of_your_certificate']
    if request.method=="POST":
        try:
            user=User.objects.get(username=email)
            return render(request,"singup.html",{'error':"User already exists"})  
        except User.DoesNotExist:
            user=User.objects.create_user(username=email,password=password,first_name=name)
            tfm=UserTeacher(NAME=name,DESIGNATION=designation,DEPARTMENT=department,DATE_OF_JOINING=date_of_join,
                ACADEMIC_QUALIFICATION=academic_qualification,EXPERIENCE=experience,GENDER=gender,
                VOTER_ID_SMART=Voter_id_smart,DATE_OF_BIRTH=date_of_birth,ADDRESS=address,MOBILE_NO_OFFICE=mobile_office,
                MOBILE_NO_PERSINAL=mobile_personal,BIO_DATA=bio_data,
                IMAGE_1ST=image_1st,IMAGE_2ND=image_2nd,SCAND_COPY_OF_NID=scand_copy_of_nid,ALL_OF_YOUR_CERTIFICATE=all_of_your_certificate)
            tfm.save()
            return render(request,"presingup.html",{'success':"user created successfully"})

def addstudent(request):
    SL=request.POST.get("sl")
    DATE_OF_AD=request.POST.get("DATE_OF_AD")
    COLLAGE_ID=request.POST.get("COLLAGE_ID")
    BORD_ROLL=request.POST.get("BORD_ROLL")
    REGISTRATION_NUMBER=request.POST.get("REGISTRATION_NUMBER")
    STUDENT_NAME=request.POST.get("STUDENT_NAME")
    mobile_student=request.POST.get("mobile_student")
    father_name=request.POST.get("father_name")
    mother_name=request.POST.get('mother_name')
    father_number=request.POST.get("father_number")
    email=request.POST.get("user_id")
    mother_number=request.POST.get("mother_number")
    address_p=request.POST.get("address_p")
    address_l=request.POST.get('address_l')
    ssc_year=request.POST.get('ssc_year')
    group=request.POST.get('group')
    bord=request.POST.get('bord')
    gpa=request.POST.get('gpa')
    mark_sheet=request.FILES['mark_sheet']
    testmonial=request.FILES['testmonial']
    DATE_OF_BIRTH=request.POST.get('DATE_OF_BIRTH')
    RELIGION=request.POST.get('RELIGION')
    gender=request.POST.get('gender')
    District=request.POST.get('District')
    Upazila_OR_Thana=request.POST.get('Upazila_OR_Thana')
    school=request.POST.get('school')
    admition_fee=request.POST.get('admition_fee')
    tuiton_fee=request.POST.get('tuiton_fee')
    semister=request.POST.get('semister')
    total_concract=request.POST.get('total_concract')
    picture_st=request.FILES['picture_st']
    password=request.POST.get("password")
    
    if request.method=="POST":
        try:
            user=User.objects.get(username=email)
            return render(request,"presingup.html",{'error':"User already exists"})
        except User.DoesNotExist:
            user=User(username=email,password=password,first_name=STUDENT_NAME)
            sfm=UserStudent(DATE_OF_AD=DATE_OF_AD,COLLAGE_ID=COLLAGE_ID,BORD_ROLL=BORD_ROLL,REGISTRATION_NUMBER=REGISTRATION_NUMBER,
            MOBILE_NO_STUDENT=mobile_student,FATHERS_NAME=father_name,MOTHERS_NAME=mother_name,FATHER_MOBILE=father_number,MOTHERS_MOBILE=mother_number,
            ADDRESS_PARMANENT=address_p,ADDRESS_LOCAL=address_l,SSC_YEAR=ssc_year,GROUP=group,BORD=bord,GPA=gpa,SCAND_COPY_OF_MARK_SHEET=mark_sheet,
            SCAND_COPY_OF_TESTMONIAL=testmonial,DATE_OF_BIRTH=DATE_OF_BIRTH,RELIGION=RELIGION,GENDER=gender,District=District,Upazila_OR_Thana=Upazila_OR_Thana,
            SCHOOL=school,ADMITION_FEE=admition_fee,TUTION_FEE=tuiton_fee,SEMISTER_FEE=semister,TOTAL_CONCRACT=total_concract,PICTURE_STUDENT=picture_st
            )
            user.save()
            sfm.save()
            return render(request,"presingup.html",{'success':"user created successfully"})

def profile(request):

    return render(request,"profile.html")