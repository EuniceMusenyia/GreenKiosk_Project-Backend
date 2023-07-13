from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    name = models.CharField(max_length = 32)
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    contact = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):           ####self acts as string representation of the class//**
        return self.name