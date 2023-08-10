from django.shortcuts import render

# Create your views here.
from .forms import NotificationUploadForm
# from .models import Notification

# Create your views here.
def upload_notification(request):
    if request.method == "POST":
        form = NotificationUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    
    else:
        form = NotificationUploadForm()
    return render(request,"notifications/notification_upload.html",{"form":form})