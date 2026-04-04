from django.contrib import admin
from .models import Record,Prescription

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "optic", "date", "created_at")
    search_fields = ("patient__first_name", "patient__last_name", "folio")
    list_filter = ("optic", "date")
    

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "record", "date", "patient_name", "optic_name")
    search_fields = ("record__patient__first_name", "record__patient__last_name")
    list_filter = ("date",)

    def patient_name(self, obj):
        return obj.record.patient
    patient_name.short_description = "Patient"

    def optic_name(self, obj):
        return obj.record.optic
    optic_name.short_description = "Optic"