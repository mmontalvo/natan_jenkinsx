from rest_framework import serializers

from .models import Client
from .models import Trade

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'full_name', 'email', 'balance')

class TradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trade
        fields = (
          'id', 'deal_reference', 'currency_pair', 'buy_currency',
          'sell_currency', 'amount', 'rate'
        #  'client'
        )