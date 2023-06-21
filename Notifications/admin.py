from django.contrib import admin

# Register your models here.
from .models import Notifications

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ("notification_type", "date", "message", "date_created")
admin.site.register(Notifications,NotificationsAdmin)
