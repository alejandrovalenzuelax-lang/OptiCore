from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "optic", "patient", "scheduled_at", "status", "assigned_to")
    list_filter = ("status", "optic", "scheduled_at")
    search_fields = ("patient__first_name", "patient__last_name", "id")