from django.contrib import admin
from .models import Shipment

# Register your models here.
class  ShipmentAdmin(admin.ModelAdmin):
    list_display = ("shipping_services", "shipping_location","shipping_method", "handling_time","transit_time","date_created")

admin.site.register(Shipment,ShipmentAdmin)
