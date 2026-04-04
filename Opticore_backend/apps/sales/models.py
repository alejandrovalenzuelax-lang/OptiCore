from django.db import models
from django.db.models import Sum

class Sale(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("delivered", "Delivered"),
        ("canceled", "Canceled"),
    )

    optic = models.ForeignKey(
        "optics.Optic",
        on_delete=models.CASCADE,
        related_name="sales"
    )
    patient = models.ForeignKey(
        "patients.Patient",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales"
    )
    record = models.ForeignKey(
        "records.Record",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales"
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    delivery_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def update_totals(self):
        items_total = self.items.aggregate(total=Sum("total_price"))["total"] or 0
        self.subtotal = items_total
        self.total = max(self.subtotal - (self.discount or 0), 0)
        self.save(update_fields=["subtotal", "total"])

    def __str__(self):
        return f"Sale #{self.id} - {self.optic.name}"


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("inventory.Product", on_delete=models.PROTECT, related_name="sale_items")

    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.total_price = (self.unit_price or 0) * (self.quantity or 0)
        super().save(*args, **kwargs)
        if self.sale_id:
            self.sale.update_totals()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class SalePayment(models.Model):
    METHOD_CHOICES = (
        ("cash", "Cash"),
        ("card", "Card"),
        ("transfer", "Transfer"),
        ("mixed", "Mixed"),
    )

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="payments")
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} - {self.amount}"