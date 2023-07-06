from django.db import models

# Create your models here.


class Product(models.Model):
    id=models.AutoField(primary_key=True)
    ProductType=models.CharField(max_length=500)
    ProductBrand=models.CharField(max_length=500)
    ProductDetails=models.CharField(max_length=1000)
    price=models.IntegerField(max_length=100)
    ProductCount=models.IntegerField(max_length=500)
    ProductImage=models.CharField(max_length=500)

class Customers(models.Model):
    CustomerId=models.AutoField(primary_key=True)
    CustomerName=models.CharField(max_length=500)
    CustomerEmail=models.CharField(max_length=500)
    CustomerOrders=models.CharField(max_length=500)
    CustomerPassword=models.CharField(max_length=20)
    CustomerDate=models.DateField()
    

