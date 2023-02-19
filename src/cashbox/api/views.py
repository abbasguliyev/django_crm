from rest_framework.views import Response
from rest_framework import status, viewsets, permissions
from cashbox.api.selectors import cashbox_list, cashflow_list
from cashbox.api.services import create_cashbox, update_cashbox, create_cashflow, update_cashflow
from cashbox.api.serializers import CashboxSerializer, CashFlowSerializer
from cashbox.api.filters import CashboxFilter, CashFlowFilter

class CashboxViewSet(viewsets.ModelViewSet):
    queryset = cashbox_list()
    serializer_class = CashboxSerializer
    filterset_class = CashboxFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_cashbox(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_cashbox(instance=instance, **serializer.validated_data)
        return Response(serializer.data)

class CashFlowViewSet(viewsets.ModelViewSet):
    queryset = cashflow_list()
    serializer_class = CashFlowSerializer
    filterset_class = CashFlowFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        create_cashflow(executor=user, **serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_cashflow(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
    