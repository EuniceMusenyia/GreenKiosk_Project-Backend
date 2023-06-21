from django.contrib import admin

# Register your models here.
from .models import Customers

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "password","id","location","contact","date_created")
admin.site.register(Customers,CustomerAdmin)
