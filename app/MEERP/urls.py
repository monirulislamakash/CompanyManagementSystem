from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("login/",views.login,name="login"),
    path("singup/",views.singup,name="singup"),
]
