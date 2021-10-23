
from django import forms
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.forms.models import ModelForm
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "password":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
        }


        
class Techer(forms.ModelForm):
    class Meta:
        model=UserTeacher
        fields = ['user','NAME','DESIGNATION','DEPARTMENT','DATE_OF_JOINING','ACADEMIC_QUALIFICATION','EXPERIENCE','DNID','GENDER','VOTER_ID_SMART','DATE_OF_BIRTH',
        'ADDRESS','MOBILE_NO_OFFICE','MOBILE_NO_PERSINAL','EMAIL','BIO_DATA','IMAGE_1ST','IMAGE_2ND','SCAND_COPY_OF_NID','ALL_OF_YOUR_CERTIFICATE']
        widgets={
            "user":forms.Select(attrs={"class":"form-control col-lg-3"}),
            "NAME":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "DESIGNATION":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "DEPARTMENT":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "DATE_OF_JOINING":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "ACADEMIC_QUALIFICATION":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "EXPERIENCE":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "DNID":forms.Select(attrs={"class":"form-control col-lg-3"}),
            "GENDER":forms.Select(attrs={"class":"form-control col-lg-3"}),
            "VOTER_ID_SMART":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "DATE_OF_BIRTH":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "ADDRESS":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "MOBILE_NO_OFFICE":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "MOBILE_NO_PERSINAL":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "EMAIL":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "BIO_DATA":forms.Textarea(attrs={"class":"form-control col-lg-3",'rows':"3"}),
            "IMAGE_1ST":forms.FileInput(attrs={"class":"form-control col-lg-3"}),
            "IMAGE_2ND":forms.FileInput(attrs={"class":"form-control col-lg-3"}),
            "SCAND_COPY_OF_NID":forms.FileInput(attrs={"class":"form-control col-lg-3"}),
            "ALL_OF_YOUR_CERTIFICATE":forms.FileInput(attrs={"class":"form-control col-lg-3"}),
            
        }
class Student(forms.ModelForm):
    class Meta:
        model=UserStudent
        fields=['user','SL','DATE_OF_AD','COLLAGE_ID','BORD_ROLL','REGISTRATION_NUMBER','MOBILE_NO_STUDENT','FATHERS_NAME','MOTHERS_NAME',
        'FATHER_MOBILE','MOTHERS_MOBILE','ADDRESS_PARMANENT','ADDRESS_LOCAL','SSC_YEAR','GROUP','BORD','GPA','SCAND_COPY_OF_MARK_SHEET',
        'SCAND_COPY_OF_TESTMONIAL','PICTURE_STUDENT','DATE_OF_BIRTH','RELIGION','GENDER','District','Upazila_OR_Thana','SCHOOL','ADMITION_FEE','TUTION_FEE',
        'SEMISTER_FEE','TOTAL_CONCRACT','Refferred_By','Refferrer_Number','Gurdian_Name','Gurdian_Relation','Father_NID',
        'Mother_NID','Student_NID_or_Birth_Crtificate','Confirm',]
        widgets={
            "user":forms.Select(attrs={"class":"form-control col-lg-3"}),
            "SL":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "DATE_OF_AD":forms.DateInput(attrs={"class":"form-control col-lg-3",'type':'date'}),
            "COLLAGE_ID":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "BORD_ROLL":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "REGISTRATION_NUMBER":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "MOBILE_NO_STUDENT":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "FATHERS_NAME":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "MOTHERS_NAME":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "FATHER_MOBILE":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "MOTHERS_MOBILE":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "ADDRESS_PARMANENT":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "ADDRESS_LOCAL":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "SSC_YEAR":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "GROUP":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "BORD":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "GPA":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "SCAND_COPY_OF_MARK_SHEET":forms.FileInput(attrs={"class":"form-control col-lg-3"}),
            "SCAND_COPY_OF_TESTMONIAL":forms.FileInput(attrs={"class":"form-control col-lg-3"}),
            "PICTURE_STUDENT":forms.FileInput(attrs={"class":"form-control col-lg-3"}),
            "DATE_OF_BIRTH":forms.DateInput(attrs={"class":"form-control col-lg-3",'type':'date'}),
            "RELIGION":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "GENDER":forms.Select(attrs={"class":"form-control col-lg-3"}),
            "District":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Upazila_OR_Thana":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "SCHOOL":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "ADMITION_FEE":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "TUTION_FEE":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "SEMISTER_FEE":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "TOTAL_CONCRACT":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Refferred_By":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Refferrer_Number":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Gurdian_Name":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Gurdian_Relation":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Father_NID":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Mother_NID":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            "Student_NID_or_Birth_Crtificate":forms.TextInput(attrs={"class":"form-control col-lg-3"}),
            
        }