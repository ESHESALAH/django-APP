from django.db import models
from django.contrib.auth.models import User

# Create your models here.user= models.ForeignKey(User,on_delete=models.CASCADE)
     
class customers(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    id_number = models.IntegerField()
    email = models.EmailField() 




def __str__(self):
        return self.user.get_email()

class shippingaddress(models.Model):  
    customers = models.ForeignKey(customers,on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=20)
    notes = models.TextField()

    
