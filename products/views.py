from math import prod
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET','POST'])
def productsList(request):
    
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET'])
def productsDetail(request, pk):
    
    product = Product.objects.filter(pk=pk)
    serializer = ProductSerializer(product,many=True) 
    return Response(serializer.data)