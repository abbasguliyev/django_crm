from rest_framework.views import Response
from rest_framework import status, viewsets, permissions
from company.api.selectors import company_list, office_list
from company.api.services import create_company, update_company, create_office, update_office
from company.api.serializers import CompanySerializer, OfficeSerializer
from company.api.filters import CompanyFilter, OfficeFilter

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = company_list()
    serializer_class = CompanySerializer
    filterset_class = CompanyFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_company(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_company(instance=instance, **serializer.validated_data)
        return Response(serializer.data)

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = office_list()
    serializer_class = OfficeSerializer
    filterset_class = OfficeFilter
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_office(**serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        update_office(instance=instance, **serializer.validated_data)
        return Response(serializer.data)
    