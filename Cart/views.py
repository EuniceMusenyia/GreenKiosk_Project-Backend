from django.shortcuts import render
from django.shortcuts import redirect

from .forms import CartUploadForm
from .models import Cart

# Create your views here.
def upload_cart(request):
    if request.method == "POST":
        form = CartUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    
    else:
        form = CartUploadForm()
    return render(request,"cart/cart_upload.html",{"form":form})

def cart_list(request):
    cart = Cart.objects.all()
    return render (request, "cart/cart_list.html", {"carts": cart})

def cart_details(request, id):
    cart = Cart.objects.get(id = id)
    return render(request, "cart/cart_details.html",{"cart": cart})

def edit_cart_view(request,id):
    product = Cart.objects.get(id = id)
    if request.method == "POST":
        form = CartUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect("cart_detail_view", id =product.id)  

    else :
        form = CartUploadForm(instance=product)
        return render (request, "cart/edit_cart.html", {"form":form})