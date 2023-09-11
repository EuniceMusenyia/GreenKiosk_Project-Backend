from django.shortcuts import render
from django.shortcuts import redirect

from .forms import CustomerUploadForm
from .models import Customer

# Create your views here.
def upload_customer(request):
    if request.method == "POST":
        form = CustomerUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    else:
        form = CustomerUploadForm()
    return render(request,"customer/customer_upload.html",{"form":form})

def customer_list(request):
    customers = Customer.objects.all()
    return render (request, "customer/customer_list.html", {"customers": customers})

def customer_details(request, id):
    customers = Customer.objects.get(id = id)
    return render(request, "customer/customer_detail.html",{"customer":customers})

def edit_customer_view(request,id):
    product = Customer.objects.get(id = id)
    if request.method == "POST":
        form = CustomerUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect("customer_detail_view", id =product.id)  

    else :
        form = CustomerUploadForm(instance=product)
        return render (request, "customer/edit_customer.html", {"form":form})