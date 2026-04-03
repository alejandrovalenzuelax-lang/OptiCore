from django.contrib import admin
from .models import Optic

@admin.register(Optic)
class OpticAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "city", "state", "active", "created_at")
    search_fields = ("name", "slug", "city", "state")
    list_filter = ("active", "state")