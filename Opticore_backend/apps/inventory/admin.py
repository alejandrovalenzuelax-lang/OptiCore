from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "brand", "price", "stock", "optic", "is_active")
    list_filter = ("type", "is_active", "optic")
    search_fields = ("name", "brand", "code", "slug")