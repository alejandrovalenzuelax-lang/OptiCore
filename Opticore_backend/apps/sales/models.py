from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError


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

    cost_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    delivery_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_totals(self):
        items_total = self.items.aggregate(total=Sum("total_price"))["total"] or 0
        cost_total = self.items.aggregate(total=Sum("total_cost"))["total"] or 0

        self.subtotal = items_total
        self.total = max(self.subtotal - (self.discount or 0), 0)
        self.cost_total = cost_total
        self.profit = self.total - self.cost_total

        self.save(update_fields=["subtotal", "total", "cost_total", "profit"])

    def __str__(self):
        return f"Sale #{self.id} - {self.optic.name}"


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("inventory.Product", on_delete=models.PROTECT, related_name="sale_items")

    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        creating = self.pk is None
        prev_qty = 0

        if not creating:
            prev = SaleItem.objects.get(pk=self.pk)
            prev_qty = prev.quantity

        # costos
        if self.unit_cost is None or self.unit_cost == 0:
            self.unit_cost = self.product.cost or 0

        self.total_price = (self.unit_price or 0) * (self.quantity or 0)
        self.total_cost = (self.unit_cost or 0) * (self.quantity or 0)

        super().save(*args, **kwargs)

        # stock (solo si no es servicio o un paquete)
        if self.product.type not in ["service", "package"]:
            delta = (self.quantity or 0) - (prev_qty or 0)
            new_stock = (self.product.stock or 0) - delta

            if new_stock < 0:
                raise ValidationError("Stock insuficiente para este producto.")

            if delta != 0:
                self.product.stock = new_stock
                self.product.save(update_fields=["stock"])

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


@receiver(post_delete, sender=SaleItem)
def update_sale_totals_on_delete(sender, instance, **kwargs):
    if instance.product.type not in ["service", "package"]:
        instance.product.stock = (instance.product.stock or 0) + (instance.quantity or 0)
        instance.product.save(update_fields=["stock"])

    if instance.sale_id:
        instance.sale.update_totals()