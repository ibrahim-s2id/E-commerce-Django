from rest_framework import serializers
from ProjectApp.models import Product,Customers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('id','ProductType','ProductBrand','ProductDetails','price','ProductCount','ProductImage')

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields =  '__all__'
