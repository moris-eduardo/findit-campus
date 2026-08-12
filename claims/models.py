# claims/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid, random, string


class Claim(models.Model):

    class Status(models.TextChoices):
        PENDING  = 'PENDING',  'Pendiente de revisión'
        APPROVED = 'APPROVED', 'Aprobado'
        REJECTED = 'REJECTED', 'Rechazado'

    id                = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item              = models.ForeignKey('items.Item', on_delete=models.CASCADE, related_name='claims')
    student           = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='claims')
    status            = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    proof_description = models.TextField()
    admin_note        = models.TextField(blank=True)
    receipt_code      = models.CharField(max_length=25, unique=True, null=True, blank=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    resolved_at       = models.DateTimeField(null=True, blank=True)
    delivered_at      = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'claims'
        ordering = ['-created_at']
        unique_together = [['item', 'student']]

    def __str__(self):
        return f"{self.student.get_full_name()} → {self.item.name} [{self.get_status_display()}]"

    def generate_receipt_code(self):
        date_str    = timezone.now().strftime('%Y%m%d')
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return f"FC-{date_str}-{random_part}"