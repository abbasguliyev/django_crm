from django.urls import path, include
from rest_framework import routers
from product.api.views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename="category")
router.register(r'', ProductViewSet, basename="product")

urlpatterns = [
    path('', include(router.urls)),
]
