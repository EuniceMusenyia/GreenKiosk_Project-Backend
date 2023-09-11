from django.shortcuts import render

from .forms import RatingUploadForm

# Create your views here.
def upload_rating(request):
    if request.method == "POST":
        form = RatingUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    else:
        form = RatingUploadForm()
    return render(request,"rating/rating_upload.html",{"form":form})
