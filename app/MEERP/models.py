from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.contrib import auth
from django.contrib.auth.models import User,AbstractUser
from django.db.models.fields.files import FileField
from django.db.models.fields.related import ForeignKey
from django.http import request
# Create your models here.
class UserTeacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    NAME=models.CharField(max_length=50,default="")
    DESIGNATION=models.CharField(max_length=100,default="")
    DEPARTMENT=models.CharField(max_length=100,default="")
    DATE_OF_JOINING=models.CharField(max_length=50,default="")
    ACADEMIC_QUALIFICATION=models.CharField(max_length=50,default="")
    EXPERIENCE=models.CharField(max_length=50,default="")
    selectdnid=(
        ('Teacher','Teacher'),
        ('Acounts','Acounts'),
        )
    DNID=models.CharField(max_length=50,choices=selectdnid,default="Teacher")
    selectgender=(
        ('male','Male'),
        ('female','Female')
        )
    GENDER=models.CharField(max_length=50,choices=selectgender,default="Male")
    VOTER_ID_SMART=models.CharField(max_length=50,default="")
    DATE_OF_BIRTH=models.CharField(max_length=50,default="")
    ADDRESS=models.CharField(max_length=200,default="")
    MOBILE_NO_OFFICE=models.CharField(max_length=50,default="")
    MOBILE_NO_PERSINAL=models.CharField(max_length=50,default="")
    EMAIL=models.CharField(max_length=50,default="")
    BIO_DATA=models.TextField(default="")
    IMAGE_1ST=models.FileField(upload_to="static/techerprode/IMAGE_1ST",default="static/logo/logo.png")
    IMAGE_2ND=models.FileField(upload_to="static/techerprode/IMAGE_2ND",default="static/logo/logo.png")
    SCAND_COPY_OF_NID=models.FileField(upload_to="static/techerprode/SCAND_COPY_OF_NIDstatic/",default="static/logo/logo.png")
    ALL_OF_YOUR_CERTIFICATE=models.FileField(upload_to="static/techerprode/ALL_OF_YOUR_CERTIFICATE",default="static/logo/logo.png")
    def __str__(self):
        return str(self.user)
class Department(models.Model):
    Name=CharField(max_length=100)
    def __str__(self):
        return str(self.Name)
class Session(models.Model):
    Name=CharField(max_length=100)
    def __str__(self):
        return str(self.Name)
class UserStudent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    SL=models.CharField(max_length=50,default="")
    DNID=models.CharField(max_length=50,default="student")
    DATE_OF_AD=models.DateField(default="")
    COLLAGE_ID=models.CharField(max_length=50,default="",unique=True)
    BORD_ROLL=models.CharField(max_length=50,default="")
    REGISTRATION_NUMBER=models.CharField(max_length=50,default="")
    Student_Name=models.CharField(max_length=50,default="")
    Department=models.CharField(max_length=50,default="")
    Session=models.CharField(max_length=50,default="")
    MOBILE_NO_STUDENT=models.CharField(max_length=50,default="")
    FATHERS_NAME=models.CharField(max_length=50,default="")
    MOTHERS_NAME=models.CharField(max_length=50,default="")
    FATHER_MOBILE=models.CharField(max_length=50,default="")
    MOTHERS_MOBILE=models.CharField(max_length=50,default="")
    ADDRESS_PARMANENT=models.CharField(max_length=50,default="")
    ADDRESS_LOCAL=models.CharField(max_length=50,default="")
    SSC_Roll=models.CharField(max_length=50,default="")
    SSC_Registration=models.CharField(max_length=50,default="")
    SSC_YEAR=models.CharField(max_length=50,default="")
    GROUP=models.CharField(max_length=50,default="")
    BORD=models.CharField(max_length=50,default="")
    GPA=models.CharField(max_length=50,default="")
    SCAND_COPY_OF_MARK_SHEET=models.FileField(upload_to="static/student/SCAND_COPY_OF_MARK_SHEET",default="static/logo/logo.png")
    SCAND_COPY_OF_TESTMONIAL=models.FileField(upload_to="static/student/SCAND_COPY_OF_TESTMONIAL",default="static/logo/logo.png")
    PICTURE_STUDENT=models.FileField(upload_to="static/student/PICTURE_STUDENT",default="static/logo/logo.png")
    DATE_OF_BIRTH=models.DateField(default="")
    RELIGION=models.CharField(max_length=50,default="")
    selectgender=(
        ('male','Male'),
        ('female','Female')
        )
    GENDER=models.CharField(max_length=50,choices=selectgender,default="Male")
    District=models.CharField(max_length=50,default="")
    Upazila_OR_Thana=models.CharField(max_length=50,default="")
    SCHOOL=models.CharField(max_length=50,default="")
    ADMITION_FEE=models.CharField(max_length=50,default="")
    TUTION_FEE=models.CharField(max_length=50,default="")
    SEMISTER_FEE=models.CharField(max_length=50,default="")
    TOTAL_CONCRACT=models.CharField(max_length=50,default="")
    Due=models.CharField(max_length=50,default="0")
    Paid=models.CharField(max_length=50,default="0")
    Refferred_By=models.CharField(max_length=50,default="")
    Refferrer_Number=models.CharField(max_length=20,default="")
    Gurdian_Name=models.CharField(max_length=50,default="")
    Gurdian_Relation=models.CharField(max_length=50,default="")
    Father_NID=models.CharField(max_length=50,default="")
    Mother_NID=models.CharField(max_length=50,default="")
    Student_NID_or_Birth_Crtificate=models.CharField(max_length=50,default="")
    Confirm=BooleanField(default=False)

    def __str__(self):
        return str(self.user)
class Wellwisher(models.Model):
    Name=models.CharField(max_length=50)
    Phone_Number=models.CharField(max_length=50)
    Profation=models.CharField(max_length=50)
    Designation=models.CharField(max_length=50)
    Admit_Student=models.CharField(max_length=50)
    Paid=models.CharField(max_length=50)
    Comment=models.TextField()
    Last_talk=models.CharField(max_length=50)
    Zila=models.CharField(max_length=50)
    Thana_or_Upozila=models.CharField(max_length=50)
class PerformanceReport(models.Model):
    pass