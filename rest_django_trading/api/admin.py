from django.contrib import admin
from .models import Client, Trade

admin.site.register(Client)
admin.site.register(Trade)