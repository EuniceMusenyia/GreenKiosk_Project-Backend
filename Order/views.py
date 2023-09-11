from django.shortcuts import render

# Create your views here.

from .forms import OrderUploadForm
from Order.models import Order
from django.shortcuts import redirect


# Create your views here.
def upload_order(request):
    if request.method == "POST":
        form = OrderUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    else:
        form = OrderUploadForm()
    return render(request,"order/order_upload.html",{"form":form})

def order_list(request):
    order = Order.objects.all()
    return render (request, "order/order_list.html", {"orders": order})

def order_detail(request, id):
    order = Order.objects.get(id = id)
    return render(request, "order/order_details.html",{"order":order})

def edit_order_view(request,id):
    order = Order.objects.get(id = id)
    if request.method == "POST":
        form = OrderUploadForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect("order_detail_view", id =order.id)  

    else :
        form = OrderUploadForm(instance=order)
        return render (request, "order/edit_order.html", {"form":form})