from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path("users/", include("account.api.urls")),
    path("company/", include("company.api.urls")),
    path("product/", include("product.api.urls")),
    path("warehouse/", include("warehouse.api.urls")),
    path("contract/", include("contract.api.urls")),
    path("cashbox/", include("cashbox.api.urls")),
]