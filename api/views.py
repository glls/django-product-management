from rest_framework import viewsets
from products.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProtectedView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request):
        return Response({"message": "This is a protected view!"})