from django.contrib import admin

# Register your models here.
from .models import Notification

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ("notification_type", "date", "message", "date_created")
admin.site.register(Notification,NotificationsAdmin)
