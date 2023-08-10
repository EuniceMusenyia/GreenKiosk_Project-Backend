from django.urls import path

from .views import upload_cart,cart_list,cart_details,edit_cart_view
urlpatterns = [
    path("cart/upload",upload_cart, name="cart_upload_view"),
    path("cart/list",cart_list, name="cart_list_view"),
    path("cart/<int:id>", cart_details, name="cart_detail_view"),
    path("cart/edit/<int:id>/",edit_cart_view,name = "cart_edit_view"),


]
