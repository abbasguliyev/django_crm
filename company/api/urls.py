from django.urls import path, include
from rest_framework import routers
from company.api.views import CompanyViewSet, OfficeViewSet

router = routers.DefaultRouter()
router.register(r'offices', OfficeViewSet, basename="office")
router.register(r'', CompanyViewSet, basename="company")

urlpatterns = [
    path('', include(router.urls)),
]

