from django.contrib import admin

# Register your models here.
from .models import Payment

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("amount", "order_number", "status", "date","payment_method","date_created")
admin.site.register(Payment, PaymentsAdmin)


   