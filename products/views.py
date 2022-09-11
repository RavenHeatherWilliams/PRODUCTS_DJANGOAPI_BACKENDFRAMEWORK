from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import products
from .serializers import ProductsSerializer
from .models import Products
@api_view(['GET', 'POST'])
def product_list(request):

    if request.method=='GET':
         products = Products.objects.all()

         serializer = ProductsSerializer(products, many=True)

         return Response(serializer.data)
   
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT', 'DELETE'])
def products_detail(request, pk):
    products = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        serializer = ProductsSerializer(products);
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductsSerializer(products, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    




