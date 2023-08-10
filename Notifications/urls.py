from django.urls import path
from .views import upload_notification
urlpatterns = [
    path("notifications/upload",upload_notification, name="notification_upload_view"),
   
]
