from django.contrib import admin

# Register your models here.
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ("price", "quantity", "shipping_cost", "payment_options", "date_created")
admin.site.register(Cart, CartAdmin)

