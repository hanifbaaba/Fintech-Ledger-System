from django.db import models
import uuid
from djmoney.models.fields import MoneyField
from django.conf import settings

class Accounts(models.Model):
    user_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    balance = MoneyField(
        max_digits=14,
        decimal_places=2,
        currency_choices=[('USD', 'US Dollar'),('EUR', 'Euro'),('GBP','Great Britain Pound'),],
       default_currency = 'USD'
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user_uuid} - {self.balance}"