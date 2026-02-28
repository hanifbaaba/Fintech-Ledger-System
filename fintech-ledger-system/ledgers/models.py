from django.db import models

class Ledger(models.Model):
    transaction_id = models.TextField(unique=True)
    account_id = models.TextField(unique=True)
    amount = models.DecimalField(decimal_places=2, default=0,max_digits=20)
    created_at = models.DateTimeField(auto_now_add=True)