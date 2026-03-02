from django.db import transaction
from decimal import Decimal
from accounts.models import Accounts
from accounts.models import Transactions
from .models import LedgerEntry

def transfer_funds(sender_id,receiver_id,amount, idempotency_key):
    if sender_id == receiver_id:
        raise ValueError("Sender and receiver cannot be the same!")
    amount = Decimal(amount)
    
    with transaction.atomic():
        existing_tx = Transactions.objects.filter(idempotency_key=idempotency_key).first()
        
        if existing_tx:
            return existing_tx
        
        sender = Accounts.objects.select_for_update().get(id=sender_id)
        receiver = Accounts.objects.select_for_update().get(id=receiver_id)
        
        if sender.balance < amount:
            raise ValueError("Insufficient balance!")
        
        tx = Transactions.objects.create(idempotency_key=idempotency_key,amount=amount)
        
        debit = Transactions.objects.create(transaction=tx,account=sender,amount=-amount)
        credit = Transactions.objects.create(transaction=tx,accounts=receiver,amount=amount)
        
        total = debit.amount + credit.amount
        
        if total != Decimal("0.00"):
            raise ValueError("Ledger Imbalance detected")
        
        sender.balance -=amount
        receiver.balance +=amount
        
        sender.save()
        receiver.save()

        return tx
        

            