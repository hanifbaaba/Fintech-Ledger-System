from django.db import models
from accounts.models import Accounts,Transactions

class Ledger(models.Model):
    transaction_id = models.ForeignKey(Transactions,on_delete=models.CASCADE, related_name='transactions', db_index=True)
    account_id = models.ForeignKey(Accounts,on_delete=models.CASCADE, related_name='accounts', db_index=True)
    amount = models.DecimalField(decimal_places=2, default=0,max_digits=20, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

class LedgerEntry(models.Model):
    transaction = models.ForeignKey(Transactions,on_delete=models.CASCADE,  related_name='ledger_transactions')
    account = models.ForeignKey(Accounts,on_delete=models.CASCADE,  related_name='ledger_accounts',db_index=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    
    # class Meta:
    #     indexes = [
    #         models.Index(fields=['transaction'], name=['transaction']),
    #         models.Index(fields=['account'], name=['account']),
    #         models.Index(fields=['amount'],name=['amount'])
    #     ]
        