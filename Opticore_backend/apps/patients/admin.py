from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_cell", "optic", "active", "created_at")
    search_fields = ("first_name", "last_name", "phone_cell", "phone_home", "email", "folio_internal")
    list_filter = ("optic", "active")