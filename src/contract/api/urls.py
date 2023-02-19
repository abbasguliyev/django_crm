from django.urls import path, include
from rest_framework import routers
from contract.api.views import ContractViewSet, CustomerViewSet, InstallmentViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename="customer")
router.register(r'installments', InstallmentViewSet, basename="installment")
router.register(r'', ContractViewSet, basename="contract")

urlpatterns = [
    path('', include(router.urls)),
]

