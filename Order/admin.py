from django.contrib import admin

# Register your models here.
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ("quantity", "date", "total", "name","date_created")
admin.site.register(Order, OrderAdmin)
