from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Optic info", {"fields": ("optic", "role")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Optic info", {"fields": ("optic", "role")}),
    )
    list_display = ("username", "email", "role", "optic", "is_staff")