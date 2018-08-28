from django.contrib import admin
from import_export import resources
from .models import Transaction, Header, Ticker

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Header)
admin.site.register(Ticker)
