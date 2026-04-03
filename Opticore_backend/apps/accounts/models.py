from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.optics.models import Optic

class User(AbstractUser):
    email = models.EmailField(unique=True)

    ROLE_CHOICES = (
        ("owner", "Owner"),
        ("admin", "Admin"),
        ("staff", "Staff"),
        ("doctor", "Doctor"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="staff")
    

    REQUIRED_FIELDS = ["email"]
    
    optic = models.ForeignKey(
        Optic,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )

    def __str__(self):
        return self.username