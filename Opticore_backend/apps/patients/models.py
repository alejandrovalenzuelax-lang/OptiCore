from django.db import models
from django.conf import settings
from apps.optics.models import Optic

class Patient(models.Model):
    optic = models.ForeignKey(
        Optic,
        on_delete=models.CASCADE,
        related_name="patients"
    )

    folio_internal = models.CharField(max_length=50, blank=True, null=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    birth_date = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)

    phone_home = models.CharField(max_length=30, blank=True, null=True)
    phone_cell = models.CharField(max_length=30, blank=True, null=True)
    phone_work = models.CharField(max_length=30, blank=True, null=True)
    work_extension = models.CharField(max_length=10, blank=True, null=True)

    company = models.CharField(max_length=100, blank=True, null=True)
    insurance_company = models.CharField(max_length=100, blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)

    beneficiary = models.CharField(max_length=100, blank=True, null=True)
    relationship = models.CharField(max_length=50, blank=True, null=True)

    general_notes = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_patients"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"