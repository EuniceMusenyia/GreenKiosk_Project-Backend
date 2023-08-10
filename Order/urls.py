from django.urls import path

from .views import edit_order_view, order_detail, upload_order, order_list

urlpatterns = [
    path("order/upload", upload_order, name="order_upload_view"),
    path("order/list", order_list, name="order_list_view"),
    path("order/<int:id>", order_detail, name="order_detail_view"),
    path("order/edit/<int:id>/",edit_order_view,name = "order_edit_view"),

]