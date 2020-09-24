from django.contrib import admin
from .models import Product
from .models import Productcategory
from .models import Productsupplier


# Register your models here.
admin.site.register(Product)
admin.site.register(Productcategory)
admin.site.register(Productsupplier)

