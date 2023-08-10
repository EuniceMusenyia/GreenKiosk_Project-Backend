from django.shortcuts import render
from django.shortcuts import redirect

from .forms import ShipmentUploadForm
from .models import Shipment

# Create your views here.
def upload_shipment(request):
    if request.method == "POST":
        form = ShipmentUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    
    else:
        form = ShipmentUploadForm()
    return render(request,"shipment/shipment_upload.html",{"form":form})

def shipment_list(request):
    shipments = Shipment.objects.all()
    return render (request, "shipment/shipment_list.html", {"shipments": shipments})

def shipment_details(request, id):
    shipments = Shipment.objects.get(id = id)
    return render(request, "shipment/shipment_detail.html",{"shipments":shipments})

def edit_shipment_view(request,id):
    shipment = Shipment.objects.get(id = id)
    if request.method == "POST":
        form = ShipmentUploadForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
        return redirect("shipment_detail_view", id =shipment.id)  

    else :
        form = ShipmentUploadForm(instance=shipment)
        return render (request, "shipment/edit_shipment.html", {"form":form})