from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserTeacher)
admin.site.register(UserStudent)
admin.site.register(Department)
admin.site.register(Session)