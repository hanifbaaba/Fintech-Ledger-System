from django.db import models
from accounts.models import Accounts,Transactions

class Ledger(models.Model):
    transaction_id = models.ForeignKey(Transactions, related_name='transactions')
    account_id = models.ForeignKey(Accounts, related_name='accounts')
    amount = models.DecimalField(decimal_places=2, default=0,max_digits=20)
    created_at = models.DateTimeField(auto_now_add=True)

class LedgerEntry(models.Model):
    transaction = models.ForeignKey(Transactions, related_name='transactions')
    account = models.ForeignKey(Accounts, related_name='accounts')
    amount = models.DecimalField(decimal_places=2)