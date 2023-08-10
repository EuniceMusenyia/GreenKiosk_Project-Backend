from django.shortcuts import render

from .forms import PaymentUploadForm
from Payments.models import Payment
from django.shortcuts import redirect


# Create your views here.
def upload_payment(request):
    if request.method == "POST":
        form = PaymentUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    
    else:
        form = PaymentUploadForm()
    return render(request,"payment/payment_upload.html",{"form":form})

def payments_list(request):
    payments = Payment.objects.all()
    return render (request, "payment/payments_list.html", {"payments": payments})

def payment_detail(request, id):
    payment = Payment.objects.get(id = id)
    return render(request, "payment/payment_detail.html",{"payment":payment})

def edit_payment_view(request,id):
    payment = Payment.objects.get(id = id)
    if request.method == "POST":
        form = PaymentUploadForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
        return redirect("payment_detail_view", id =payment.id)  

    else :
        form = PaymentUploadForm(instance=payment)
        return render (request, "payment/edit_payment.html", {"form":form})