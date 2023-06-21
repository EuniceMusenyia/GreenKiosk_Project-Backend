from django.contrib import admin

# Register your models here.
from .models import Ratings

class RatingsAdmin(admin.ModelAdmin):
    list_display = ("review_message", "sender", "value","product","date", "date_created")
admin.site.register(Ratings,RatingsAdmin)
