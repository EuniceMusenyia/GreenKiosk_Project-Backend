from django.contrib import admin

# Register your models here.
from .models import Payments

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("amount", "order", "status", "date","payment_method","date_created")
admin.site.register(Payments, PaymentsAdmin)


   