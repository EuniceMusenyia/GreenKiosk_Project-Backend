from django.contrib import admin

# Register your models here.
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "password","id","location","contact","date_created")
admin.site.register(Customer,CustomerAdmin)
