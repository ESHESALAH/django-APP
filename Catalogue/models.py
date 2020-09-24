from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Productsupplier(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    email=models.EmailField()

    street_address=models.CharField(max_length=50)

    phone_number=models.IntegerField()

    id_number=models.IntegerField()

    date_added =models.DateField()

    profile_picture=models.ImageField()
    
    def __str__(self):
        return self.street_address


class Productcategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    Icon = models.ImageField()   
    
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=20)
  
    category = models.ForeignKey(Productcategory,on_delete=models.CASCADE)

    description = models.TextField()

    supplier_price = models.DecimalField(max_digits=50, decimal_places=2)

    selling_price = models.DecimalField(max_digits=50, decimal_places=2)

    supplier = models.ForeignKey(Productsupplier,on_delete=models.CASCADE)

    #kiosk = models.ForeignKey(Kiosk,on_delete=models.CASCADE)

    number_in_stock = models.IntegerField()
    product_image = models.ImageField(upload_to='gallery/')

     
    def __str__(self):
        return self.title










