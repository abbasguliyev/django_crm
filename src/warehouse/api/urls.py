from django.urls import path, include
from rest_framework import routers
from warehouse.api.views import WarehouseViewSet, StockViewSet

router = routers.DefaultRouter()
router.register(r'stocks', StockViewSet, basename="stock")
router.register(r'', WarehouseViewSet, basename="warehouse")

urlpatterns = [
    path('', include(router.urls)),
]
