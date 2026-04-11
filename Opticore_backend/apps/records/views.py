from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from weasyprint import HTML
from .models import Record

class PrescriptionPdfView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, record_id):
        record = get_object_or_404(
            Record.objects.select_related("patient", "optic"),
            id=record_id
        )

        # Seguridad opcional: tu usuario solo ve sus ópticas
        if request.user.optic_id and (request.user.optic_id != record.optic_id):
            return HttpResponse(status=403)

        prescription = getattr(record, "prescription", None)
        if not prescription:
            return HttpResponse("Este expediente no tiene receta.", status=404)

        context = {
            "record": record,
            "prescription": prescription,
            "patient": record.patient,
            "optic": record.optic,
            "date": prescription.date or record.date or timezone.localdate(),
            "patient_age": prescription.patient_age or record.patient.age,
        }

        html_string = render_to_string("records/prescription_pdf.html", context)
        pdf_file = HTML(string=html_string).write_pdf()
        filename = f"prescription_record_{record.id}.pdf"
        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        return response