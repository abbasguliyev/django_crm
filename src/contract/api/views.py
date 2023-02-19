from rest_framework.views import Response
from rest_framework import status, viewsets, permissions
from contract.api.selectors import contract_list, customer_list, installment_list
from contract.api.services import create_contract, update_contract, create_customer, update_customer, create_installment, update_installment
from contract.api.serializers import CustomerSerializer, ContractSerializer, InstallmentSerializer
from contract.api.filters import CustomerFilter, ContractFilter, InstallmentFilter

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = customer_list()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_customer(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_customer(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
    

class ContractViewSet(viewsets.ModelViewSet):
    queryset = contract_list()
    serializer_class = ContractSerializer
    filterset_class = ContractFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_contract(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_contract(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
    
class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = installment_list()
    serializer_class = InstallmentSerializer
    filterset_class = InstallmentFilter
    http_method_names = ['get', 'head']

    