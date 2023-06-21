from django.db import models

# Create your models here.
class Cart (models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveBigIntegerField()
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2)
    payment_options = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):           ####self acts as string representation of the class//**
        return self.payment_options