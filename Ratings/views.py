from django.shortcuts import render

from .forms import RatingUploadForm

# Create your views here.
def upload_rating(request):
    if request.method == "POST":
        form = RatingUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    
    else:
        form = RatingUploadForm()
    return render(request,"rating/rating_upload.html",{"form":form})
