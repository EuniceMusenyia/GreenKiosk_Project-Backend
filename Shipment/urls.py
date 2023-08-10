from django.urls import path

from .views import upload_shipment,shipment_list,shipment_details, edit_shipment_view

urlpatterns = [
    path("shipment/upload",upload_shipment, name="shipment_upload_view"),
    path("shipment/list",shipment_list, name="shipment_list_view"),
    path("shipment/<int:id>", shipment_details, name="shipment_detail_view"),
    path("shipment/edit/<int:id>/",edit_shipment_view,name = "customer_edit_view"),


]
