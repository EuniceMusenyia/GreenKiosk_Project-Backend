from django.urls import path

from .views import upload_vendor, vendors_list, vendor_detail,edit_vendor_view

urlpatterns = [
    path("Vendor/upload", upload_vendor, name="vendor_upload_view"),
    path("Vendor/list", vendors_list, name="vendors_list_view"),
    path("Vendor/<int:id>", vendor_detail, name="vendor_detail_view"),
    path("Vendor/edit/<int:id>/",edit_vendor_view,name = "vendor_edit_view"),

]