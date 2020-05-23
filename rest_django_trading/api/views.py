from rest_framework import viewsets

from .serializers import ClientSerializer, TradeSerializer
from .models import Client, Trade

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer