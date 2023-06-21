from django.db import models

# Create your models here.
class  Delivery(models.Model):
    date = models.DateField()
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2)
    order_status = models.CharField(max_length=32)
    delivery_duration = models.DurationField()
    delivery_person = models.CharField(max_length=32)
    delivery_method = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):           ####self acts as string representation of the class//**
        return self.order_status