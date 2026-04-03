from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    TYPE_CHOICES = (
        ("frame", "Frame"),
        ("lens", "Lens"),
        ("accessory", "Accessory"),
        ("service", "Service"),
    )

    optic = models.ForeignKey(
        "optics.Optic",
        on_delete=models.CASCADE,
        related_name="products"
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    brand = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(default=0)
    min_stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.optic.name})"