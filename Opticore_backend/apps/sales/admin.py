from django.contrib import admin
from .models import Sale, SaleItem, SalePayment

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1

class SalePaymentInline(admin.TabularInline):
    model = SalePayment
    extra = 1

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "optic", "patient", "status", "total", "delivery_date", "created_at")
    list_filter = ("status", "optic", "delivery_date")
    search_fields = ("patient__first_name", "patient__last_name", "id")
    inlines = [SaleItemInline, SalePaymentInline]

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ("sale", "product", "quantity", "unit_price", "total_price")

@admin.register(SalePayment)
class SalePaymentAdmin(admin.ModelAdmin):
    list_display = ("sale", "method", "amount", "paid_at")
    list_filter = ("method",)