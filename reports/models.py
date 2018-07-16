from django.db import models

# Create your models here.
class Transaction(models.Model):
    prim_key = models.CharField(max_length=300, primary_key=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    transtype = models.CharField(max_length=20, null=True, blank=True)
    symbol = models.CharField(max_length=100, null=True, blank=True)
    tradedate = models.DateField(null=True, blank=True)
    broker = models.CharField(max_length=150, null=True, blank=True)
    shareamount = models.IntegerField(null=True, blank=True)
    buyprice = models.FloatField(null=True, blank=True)
    sellprice = models.FloatField(null=True, blank=True)
    commiss = models.FloatField(null=True, blank=True)
    dealsize = models.FloatField(null=True, blank=True)
    dealprice = models.FloatField(null=True, blank=True)
    leadbroker = models.CharField(max_length=150, null=True, blank=True)
    percsellhold = models.FloatField(null=True, blank=True)
    opentraddat = models.DateField(null=True, blank=True)
    vwaptraddat = models.DateField(null=True, blank=True)
    closetraddat = models.DateField(null=True, blank=True)
    prevclose = models.FloatField(null=True, blank=True)
    t2close = models.FloatField(null=True, blank=True)
    t3close = models.FloatField(null=True, blank=True)
    t4close = models.FloatField(null=True, blank=True)
    t5close = models.FloatField(null=True, blank=True)
    spopen = models.FloatField(null=True, blank=True)
    spclose = models.FloatField(null=True, blank=True)
    matching = models.CharField(max_length=1000, null=True, blank=True)
    matching_amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.prim_key

class Header(models.Model):
    inp_head = models.CharField(max_length=250, primary_key=True)
    out_head = models.CharField(max_length=250)

    def __str__(self):
        return self.inp_head

class Ticker(models.Model):
    inp_ticker = models.CharField(max_length=250, primary_key=True)
    standard_ticker = models.CharField(max_length=30)

    def __str__(self):
        return self.inp_ticker

class Broker(models.Model):
    inp_broker = models.CharField(max_length=250, primary_key=True)
    standard_broker = models.CharField(max_length=100)

    def __str__(self):
        return self.inp_broker
