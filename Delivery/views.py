from django.shortcuts import render

from django.shortcuts import redirect

from .forms import DeliveryUploadForm
from Delivery.models import Delivery

# Create your views here.
def upload_delivery(request):
    if request.method == "POST":
        form = DeliveryUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    else:
        form = DeliveryUploadForm()
    return render(request,"delivery/delivery_upload.html",{"form":form})

def delivery_list(request):
    delivery = Delivery.objects.all()
    return render (request, "delivery/delivery_list.html", {"deliveries": delivery})


def delivery_detail(request, id):
    delivery = Delivery.objects.get(id = id)
    return render(request, "delivery/delivery_detail.html",{"delivery":delivery})

def edit_delivery_view(request,id):
    delivery = Delivery.objects.get(id = id)
    if request.method == "POST":
        form = DeliveryUploadForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
        return redirect("payment_detail_view", id =delivery.id)  

    else :
        form = DeliveryUploadForm(instance=delivery)
        return render (request, "delivery/edit_delivery.html", {"form":form})