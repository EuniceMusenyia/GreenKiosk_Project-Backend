from django.db import models

# Create your models here.
class Payment(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    order_number = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    date = models.DateField()
    payment_method = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):           ####self acts as string representation of the class//**
        return self.status