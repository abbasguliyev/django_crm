from django.urls import path, include
from rest_framework import routers
from company.api.views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'', CompanyViewSet, basename="company")

urlpatterns = [
    path('', include(router.urls)),
]
