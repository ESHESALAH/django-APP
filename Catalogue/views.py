from django.shortcuts import render
from .import views
from .models import Product



# Create your views here.

def products_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})

def upload_product(request):
    form = ProductForm()
    return render(request, 'upload_product.html',{'form':form})