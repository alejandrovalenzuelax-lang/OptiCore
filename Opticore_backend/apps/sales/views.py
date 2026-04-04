from datetime import datetime
from django.utils import timezone
from django.db.models import Sum, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Sale


class DailySalesReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # fecha: ?date=YYYY-MM-DD (si no viene, usa hoy)
        date_str = request.query_params.get("date")
        if date_str:
            try:
                report_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                return Response({"detail": "Formato de fecha inválido. Usa YYYY-MM-DD."}, status=400)
        else:
            report_date = timezone.localdate()

        # óptica del usuario
        optic = getattr(request.user, "optic", None)
        if not optic:
            return Response({"detail": "El usuario no tiene óptica asignada."}, status=400)

        qs = Sale.objects.filter(optic=optic, created_at__date=report_date)

        data = qs.aggregate(
            sales_count=Count("id"),
            total_sales=Sum("total"),
            total_paid=Sum("paid_total"),
            total_pending=Sum("pending_total"),
            total_cost=Sum("cost_total"),
            total_profit=Sum("profit"),
        )

        # normalizar None -> 0
        for k, v in data.items():
            data[k] = v or 0

        return Response({
            "date": report_date,
            "optic_id": optic.id,
            "optic_name": optic.name,
            **data
        })