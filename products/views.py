from rest_framework.decorators import api_view
from rest_framework.response import Response

import products
from .serializers import ProductsSerializer
from .models import Products
@api_view(['GET'])
def product_list(request):

    products = Products.objects.all()

    serializer = ProductsSerializer(products, many=True)

    return Response(serializer.data)
