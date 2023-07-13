from django.db import models
from Order.models import Order

# Create your models here.
class Shipment (models.Model):
    Order = models.ManyToManyField(Order)

    shipping_services = models.DateField(auto_created=True)
    shipping_location = models.CharField(max_length=32)
    shipping_method = models.CharField(max_length=32)
    handling_time =models.DurationField()
    transit_time = models.DurationField()
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shipping_method
