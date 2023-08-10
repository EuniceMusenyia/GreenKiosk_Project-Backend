from django.urls import path

from .views import upload_payment, payments_list, payment_detail, edit_payment_view

urlpatterns = [
    path("Payments/upload", upload_payment, name="payment_upload_view"),
    path("Payments/list", payments_list, name="payments_list_view"),
    path("Payments/<int:id>", payment_detail, name="payment_detail_view"),
    path("Payments/edit/<int:id>/",edit_payment_view,name = "payment_edit_view"),

]