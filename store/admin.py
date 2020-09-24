from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'inventory_on_hand', 'available', 'created', 'updated']
    list_editable = ['cost', 'inventory_on_hand', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(models.Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'customerName', 'emailAddress', 'address', 'phoneNumber']
    list_per_page = 20


admin.site.register(models.Purchase, OrderAdmin)
