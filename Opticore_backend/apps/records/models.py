from django.db import models
from django.conf import settings
from apps.optics.models import Optic
from apps.patients.models import Patient

class Record(models.Model):
    optic = models.ForeignKey(
        Optic,
        on_delete=models.CASCADE,
        related_name="records"
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="records"
    )

    folio = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    general_observations = models.TextField(blank=True, null=True)

    # RX anterior
    rx_prev_od_sph = models.CharField(max_length=20, blank=True, null=True)
    rx_prev_od_cyl = models.CharField(max_length=20, blank=True, null=True)
    rx_prev_od_axis = models.CharField(max_length=20, blank=True, null=True)
    rx_prev_od_add = models.CharField(max_length=20, blank=True, null=True)

    rx_prev_oi_sph = models.CharField(max_length=20, blank=True, null=True)
    rx_prev_oi_cyl = models.CharField(max_length=20, blank=True, null=True)
    rx_prev_oi_axis = models.CharField(max_length=20, blank=True, null=True)
    rx_prev_oi_add = models.CharField(max_length=20, blank=True, null=True)

    # Historial visual y médico
    photophobia = models.BooleanField(default=False)
    irritation = models.BooleanField(default=False)
    burning = models.BooleanField(default=False)
    tearing = models.BooleanField(default=False)
    headache = models.BooleanField(default=False)
    blurred_vision = models.BooleanField(default=False)
    near_vision = models.BooleanField(default=False)
    far_vision = models.BooleanField(default=False)

    glaucoma = models.BooleanField(default=False)
    ocular_trauma = models.BooleanField(default=False)
    strabismus = models.BooleanField(default=False)
    uveitis = models.BooleanField(default=False)
    keratoconus = models.BooleanField(default=False)
    pterygium = models.BooleanField(default=False)
    stye = models.BooleanField(default=False)
    conjunctivitis = models.BooleanField(default=False)

    diabetes = models.BooleanField(default=False)
    blood_pressure = models.CharField(max_length=50, blank=True, null=True)
    heart_condition = models.BooleanField(default=False)
    surgeries = models.TextField(blank=True, null=True)

    uses_glasses = models.BooleanField(default=False)
    glasses_use_time = models.CharField(max_length=50, blank=True, null=True)

    # RX actual
    rx_od_sph = models.CharField(max_length=20, blank=True, null=True)
    rx_od_cyl = models.CharField(max_length=20, blank=True, null=True)
    rx_od_axis = models.CharField(max_length=20, blank=True, null=True)
    rx_od_add = models.CharField(max_length=20, blank=True, null=True)

    rx_oi_sph = models.CharField(max_length=20, blank=True, null=True)
    rx_oi_cyl = models.CharField(max_length=20, blank=True, null=True)
    rx_oi_axis = models.CharField(max_length=20, blank=True, null=True)
    rx_oi_add = models.CharField(max_length=20, blank=True, null=True)

    # Lente y armazón
    lens_type = models.CharField(max_length=100, blank=True, null=True)
    lens_observations = models.TextField(blank=True, null=True)
    di = models.CharField(max_length=20, blank=True, null=True)
    alt = models.CharField(max_length=20, blank=True, null=True)

    frame_brand = models.CharField(max_length=100, blank=True, null=True)
    frame_model = models.CharField(max_length=100, blank=True, null=True)
    frame_color = models.CharField(max_length=50, blank=True, null=True)
    frame_size = models.CharField(max_length=50, blank=True, null=True)

    # Atención y seguimiento
    optometrist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="optometrist_records"
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="seller_records"
    )

    delivery_date = models.DateField(blank=True, null=True)
    delivery_notes = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_records"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Record {self.id} - {self.patient}"