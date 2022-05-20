from urllib import response
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreate

# Create your views here.
# def home(request):
#     return render(request,'home.html')

class Signupview(CreateView):
    form_class=UserCreate
    success_url = reverse_lazy('login')
    template_name='signup.html'