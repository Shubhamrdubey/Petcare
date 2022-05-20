from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import CustomUser
from .forms import UserCreate, UserChange

class CustomAdmin(UserAdmin):  
    model=CustomUser
    form=UserChange
    added_form=UserCreate
    list_display=['username','email','is_staff','Age',\
        'Number','Profession','Gender','Address']



admin.site.register(CustomUser,CustomAdmin)