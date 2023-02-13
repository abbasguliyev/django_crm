from django.contrib import admin
from warehouse.models import Warehouse, Stock

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'office', 'address')
    list_display_links = ('id', 'name')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'warehouse', 'product', 'quantity')
    list_display_links = ('id',)