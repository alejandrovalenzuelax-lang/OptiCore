from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "optic", "date", "created_at")
    search_fields = ("patient__first_name", "patient__last_name", "folio")
    list_filter = ("optic", "date")