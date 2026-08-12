# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Estudiante'
        ADMIN   = 'ADMIN',   'Administrador (Prefectura)'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT
    )
    matricula = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )
    institutional_email = models.EmailField(
        unique=True
    )
    phone = models.CharField(
        max_length=15,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'institutional_email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.get_full_name()} ({self.matricula or 'Admin'})"