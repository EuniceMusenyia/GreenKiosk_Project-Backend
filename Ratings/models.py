from django.db import models

# Create your models here.
class Ratings(models.Model):
    review_message = models.TextField(max_length =100)
    sender = models.CharField(max_length=32)
    value = models.PositiveIntegerField()
    date = models.DateField()
    product = models.CharField(max_length=32)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):           ####self acts as string representation of the class//**
        return self.sender