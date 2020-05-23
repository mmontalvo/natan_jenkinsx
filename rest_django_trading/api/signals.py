# from django.db import models
# from django.dispatch import receiver
# from django.core.signals import post_save
# from apps.models import Trade

# import requests

# @receiver(post_save, sender=Trade)
# def ensure_payment_delivery(self, instance, **kwargs):
#     if kwargs.get('created', False):
#         payload = {
#             'deal_reference': instance.deal_reference,
#             'currency_pair':  instance.currency_pair,
#             'buy_currency':   instance.buy_currency,
#             'sell_currency':  instance.sell_currency,
#             'amount':         instance.amount,
#             'client_id':      instance.client_id
#         }
#         requests.post("http://payments/api/payment", data=payload)