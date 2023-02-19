from rest_framework.views import Response
from rest_framework import status, viewsets, permissions
from product.api.selectors import product_list, category_list
from product.api.services import create_product, update_product, create_category, update_category
from product.api.serializers import ProductSerializer, CategorySerializer
from product.api.filters import ProductFilter, CategoryFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = category_list()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_category(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_category(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = product_list()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_product(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_product(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
    