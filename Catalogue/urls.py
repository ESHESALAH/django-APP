from django.urls import path
from .views import upload_product
from .import views
from .views import products_list


urlpatterns = [
    path("product/", products_list, name = "products_list"),
    path("product/upload/", upload_product, name="product-uploads")
]