from rest_framework.views import Response
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from warehouse.api.selectors import warehouse_list, stock_list
from warehouse.api.services import create_warehouse, update_warehouse, create_stock, update_stock, add_product_to_stock, reduce_product_from_stock
from warehouse.api.serializers import WarehouseSerializer, StockSerializer, ChangeQuantityStockSerializer
from warehouse.api.filters import WarehouseFilter, StockFilter

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = warehouse_list()
    serializer_class = WarehouseSerializer
    filterset_class = WarehouseFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_warehouse(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_warehouse(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
    
class StockViewSet(viewsets.ModelViewSet):
    queryset = stock_list()
    serializer_class = StockSerializer
    filterset_class = StockFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_stock(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_stock(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
    
    @action(methods=["POST"], detail=False, serializer_class=ChangeQuantityStockSerializer, url_path="increase-stock")
    def increase_stock(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        add_product_to_stock(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(methods=["POST"], detail=False, serializer_class=ChangeQuantityStockSerializer, url_path="decrease-stock")
    def decrease_stock(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reduce_product_from_stock(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    