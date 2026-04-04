from datetime import timedelta
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

class Appointment(models.Model):
    STATUS_CHOICES = (
        ("scheduled", "Scheduled"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
        ("no_show", "No Show"),
    )

    optic = models.ForeignKey(
        "optics.Optic",
        on_delete=models.CASCADE,
        related_name="appointments"
    )
    patient = models.ForeignKey(
        "patients.Patient",
        on_delete=models.CASCADE,
        related_name="appointments"
    )
    record = models.ForeignKey(
        "records.Record",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="appointments"
    )

    scheduled_at = models.DateTimeField()
    duration_minutes = models.IntegerField(default=30)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="scheduled")

    reason = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_appointments"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_appointments"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def end_time(self):
        return self.scheduled_at + timedelta(minutes=self.duration_minutes or 0)

    def clean(self):
        if not self.scheduled_at:
            return

        qs = Appointment.objects.filter(
            optic=self.optic,
            scheduled_at__date=self.scheduled_at.date()
        )
        if self.assigned_to_id:
            qs = qs.filter(assigned_to=self.assigned_to)
        if self.pk:
            qs = qs.exclude(pk=self.pk)

        for appt in qs:
            appt_end = appt.scheduled_at + timedelta(minutes=appt.duration_minutes or 0)
            if appt.scheduled_at < self.end_time() and appt_end > self.scheduled_at:
                raise ValidationError("Esta cita se cruza con otra cita existente.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Appointment #{self.id} - {self.patient}"