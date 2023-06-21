from django.contrib import admin

# Register your models here.
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "contact", "password","store_name", "user_name", "date_created")
admin.site.register(Vendor, VendorAdmin)
