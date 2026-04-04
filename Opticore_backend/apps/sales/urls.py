from django.urls import path
from .views import DailySalesReportView

urlpatterns = [
    path("reports/daily/", DailySalesReportView.as_view(), name="daily-sales-report"),
]