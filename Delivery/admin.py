from django.contrib import admin

# Register your models here.
from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("date", "delivery_cost", "order_status","delivery_duration","delivery_person","delivery_method", "date_created")
admin.site.register(Delivery,DeliveryAdmin)

