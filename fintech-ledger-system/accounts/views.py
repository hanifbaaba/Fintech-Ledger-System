from django.shortcuts import render
from .models import Accounts,Transactions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AccountsView(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    # serializer_class = AccountsSerializer
    # permission_classes = [IsAuthenticated]
    

class TransactionsView(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    # serializer_class = TransactionsSerializer
    # permission_classes = [IsAuthenticated]