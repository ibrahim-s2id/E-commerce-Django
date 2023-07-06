from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ProjectApp.models import Product,Customers
from ProjectApp.serializers import ProductSerializer,CustomersSerializer
from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def ProductApi(request,id=0):
    if request.method=='GET':
        products=Product.objects.all()
        products_serializer=ProductSerializer(products,many=True)
        return JsonResponse(products_serializer.data,safe=False)
    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        products_serializer=ProductSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        product_data=JSONParser().parse(request)
        product=Product.objects.get(id=product_data['id'])
        products_serializer=ProductSerializer(product,data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        product=Product.objects.get(id=id)
        product.delete()
        return JsonResponse("Deleted Successfully",safe=False)
@csrf_exempt
def Updateorder(request):
    if request.method=='PUT':
        user_data=JSONParser().parse(request)
        Customer= Customers.objects.get(CustomerId=user_data['CustomerId'])
        user_serializer = CustomersSerializer(Customer)
        x={
            "CustomerId":user_serializer.data['CustomerId'],
            "CustomerName":user_serializer.data['CustomerName'],
            "CustomerEmail":user_serializer.data['CustomerEmail'],
            "CustomerOrders":user_data['CustomerOrders'],
            "CustomerPassword":user_serializer.data['CustomerPassword'],
            "CustomerDate":user_serializer.data['CustomerDate'],

        }
        User_serializer=CustomersSerializer(Customer,data=x)
        if User_serializer.is_valid():
            User_serializer.save()
            return JsonResponse("the pay is success" , safe=False)
        return JsonResponse("Failed to Update.",safe=False)
@csrf_exempt
def Getorder(request):
    if request.method=='POST':
        counter = JSONParser().parse(request)
        Customer=Customers.objects.get(CustomerId=counter['CustomerId'])
        u_serializer=CustomersSerializer(Customer)
        return JsonResponse(u_serializer.data['CustomerOrders'], safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)

@csrf_exempt    
def ViewCustomers(request,id=0):
    if request.method=='GET':
        View_Customers=Customers.objects.all()
        Customers_Serializer=CustomersSerializer(View_Customers,many=True)
        return JsonResponse(Customers_Serializer.data,safe=False)

@csrf_exempt
def LoginUser(request,id=0):
    if request.method=='POST':
        Customer_data=JSONParser().parse(request)
        for i in Customers.objects.all():
            if i.CustomerEmail==Customer_data['CustomerEmail'] and i.CustomerPassword== Customer_data['CustomerPassword']:
                Cus= CustomersSerializer(i)
                return JsonResponse(Cus.data['CustomerId'], safe=False)
        return JsonResponse("Not found!!", safe=False)

@csrf_exempt
def RegisterCustomers(request,id=0):
    if  request.method=='POST':
        Customer_data=JSONParser().parse(request)
        customer_serializer = CustomersSerializer(data=Customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add.",safe=False)

