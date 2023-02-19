from django.contrib import admin
from company.models import Company, Office

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "company", "is_main")
    list_display_links = ("id", "name")