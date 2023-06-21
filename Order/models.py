from django.db import models

# Create your models here.
class Order(models.Model):
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=32)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):           ####self acts as string representation of the class//**
        return self.name