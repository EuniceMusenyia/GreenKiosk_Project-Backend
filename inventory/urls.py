from django.urls import path

from .views import  products_list, upload_product,product_detail,add_to_cart,edit_product_view



urlpatterns = [
    path("products/upload", upload_product, name="products_upload_view"),
    path("products/list", products_list, name="products_list_view"),
    path("products/<int:id>", product_detail, name="product_detail_view"),
    path("add_to_cart/",add_to_cart,name='add_to_cart_view'),
    path("products/edit/<int:id>/",edit_product_view,name = "product_edit_view"),
]


