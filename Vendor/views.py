from django.shortcuts import render

# Create your views here.

from .forms import VendorUploadForm
from Vendor.models import Vendor
from django.shortcuts import redirect


# Create your views here.
def upload_vendor(request):
    if request.method == "POST":
        form = VendorUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    
    else:
        form = VendorUploadForm()
    return render(request,"vendor/vendor_upload.html",{"form":form})

def vendors_list(request):
    vendors = Vendor.objects.all()
    return render (request, "vendor/vendors_list.html", {"vendors": vendors})

def vendor_detail(request, id):
    vendor= Vendor.objects.get(id = id)
    return render(request, "vendor/vendor_detail.html",{"vendor":vendor})

def edit_vendor_view(request,id):
    vendor = Vendor.objects.get(id = id)
    if request.method == "POST":
        form = VendorUploadForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
        return redirect("payment_detail_view", id =vendor.id)  

    else :
        form = VendorUploadForm(instance=vendor)
        return render (request, "vendor/edit_vendor.html", {"form":form})
