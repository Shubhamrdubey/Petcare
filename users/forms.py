from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import CustomUser

class UserCreate(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields=('first_name','last_name','email','Age','Number',
        'Profession','Gender','Address','username')

class UserChange(UserChangeForm):
    class Meta(UserChangeForm):
        model=CustomUser
        fields=UserChangeForm.Meta.fields
        fields=('username','first_name','last_name','email','Age','Address','Gender','Number',
        'Profession')