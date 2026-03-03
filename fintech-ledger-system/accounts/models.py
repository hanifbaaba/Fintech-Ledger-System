from django.db import models
import uuid
from django.conf import settings

class Accounts(models.Model):
    user_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user_uuid} - {self.balance}"

class Transactions(models.Model):
    idempotency_key = models.CharField(unique=True)
    reference = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_OPTIONS = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_OPTIONS,
        default='PENDING'
    )