from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "optic", "created_at")
    search_fields = ("first_name", "last_name", "phone", "email")
    list_filter = ("optic",)