from django.urls import path, include
from rest_framework import routers
from cashbox.api.views import CashboxViewSet, CashFlowViewSet

router = routers.DefaultRouter()
router.register(r'cashflow', CashFlowViewSet, basename="cashflow")
router.register(r'', CashboxViewSet, basename="cashbox")

urlpatterns = [
    path('', include(router.urls)),
]

