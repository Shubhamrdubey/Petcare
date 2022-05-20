from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    Male='Male'
    Female='Female'
    Others='Others'
    gen=[(Male,'Male'),(Female,'Female'),(Others,'Others')]
    
    Age=models.PositiveIntegerField(null=True,blank=True)
    Address=models.TextField(null=True,blank=True)
    Gender=models.CharField(null=True,choices=gen,max_length=10)
    Number=models.PositiveIntegerField(null=True,unique=True)
    Profession=models.CharField(null=True,blank=True,max_length=50)

    
    