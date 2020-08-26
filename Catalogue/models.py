from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class productsupplier(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    email=models.EmailField()

    street_address=models.CharField(max_length=50)

    phone_number=models.IntegerField()

    id_number=models.IntegerField()

    date_added =models.DateField()

    profile_picture=models.ImageField()
    
    def __str__(self):
        return self.user.get_street_address()



class productcategory(models.Model):
    name = models.CharField(max_length=4)
    description = models.TextField()
    Icon = models.ImageField()   
    
    def __str__(self):
        return self.name


class product(models.Model):
    title = models.CharField(max_length=5)
  
    category = models.ForeignKey(productcategory,on_delete=models.CASCADE)

    description = models.TextField()

    supplier_price = models.DecimalField(max_digits=50, decimal_places=2)

    selling_price = models.DecimalField(max_digits=50, decimal_places=2)

    supplier = models.ForeignKey(productsupplier,on_delete=models.CASCADE)

    #Kiosk = models.ForeignKey(Kiosk,on_delete=models.CASCADE)

    number_in_stock = models.IntegerField()
     
    def __str__(self):
        return self.Kiosk










