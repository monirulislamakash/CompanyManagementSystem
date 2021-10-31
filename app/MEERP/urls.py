from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("singup/",views.singup,name="singup"),
    path("presingup/",views.presingup,name="presingup"),
    path("addusertecher/",views.addusertecher,name="addusertecher"),
    path("addstudent/",views.addstudent,name="addstudent"),
    path('profile/',views.profile,name="profile"),
    path('adduser/',views.adduser,name="adduser"),
    path('accounts/',views.accounts,name="accounts"),
    path('studentsearch/',views.studentsearch,name="studentsearch"),
    path('studentsearchpro/',views.studentsearchpro,name="studentsearchpro")
]
