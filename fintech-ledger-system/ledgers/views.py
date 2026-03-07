from django.shortcuts import render
from .models import Ledger
from .serializers import LedgerSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import transfer_funds
from rest_framework.permissions import IsAuthenticated

from rest_framework.permissions import IsAuthenticated
from django.db import transaction


class LedgerView(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = LedgerSerializer
    
    
class TransferView(APIView):
    permission_classes=[IsAuthenticated]
    # serializer_classes = 
    
    def post(self,request):
        sender = request.data['sender']
        receiver = request.data['receiver']
        amount = request.data ['amount']
        idempotency_key = request.data ['idempotency_key']
        
        tx =transfer_funds(sender,receiver,amount,idempotency_key)
        return Response ({"transaction_id":tx.id})
