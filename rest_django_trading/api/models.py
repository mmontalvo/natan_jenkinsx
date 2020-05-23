import uuid
from django.db import models

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=128)
    email = models.CharField(max_length=256)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

class Trade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deal_reference = models.CharField(max_length=128)
    currency_pair = models.CharField(max_length=8)
    buy_currency = models.CharField(max_length=4)
    sell_currency = models.CharField(max_length=4)
    amount = models.IntegerField(default=0)
    rate = models.FloatField(default=0.0)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.deal_reference