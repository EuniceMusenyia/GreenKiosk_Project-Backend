from django.db import models
from Vendor.models import Vendor
from Payments.models import Payment
from customer.models import Customer

class Order(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=32)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name