from django.urls import path
from .views import PrescriptionPdfView

urlpatterns = [
    path("<int:record_id>/prescription-pdf/", PrescriptionPdfView.as_view(), name="prescription-pdf"),
]

