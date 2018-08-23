import json
from django import forms
from django.contrib.auth.models import User
from .models import Transaction

class TickerForm(forms.Form):
    inpTick = forms.CharField(label='Ticker on Input Sheet')
    outTick = forms.CharField(label='Stock Ticker')

    def __init__(self, user, *args, **kwargs):
        super(TickerForm, self).__init__(*args, **kwargs)
        self.user = user

class HeaderForm(forms.Form):
    HEADER_OPTIONS = ()
    for i in Transaction._meta.get_fields():
        i = str(i).replace('reports.Transaction.', '')
        choice = (i, i)
        if choice not in HEADER_OPTIONS:
            HEADER_OPTIONS += (choice),

    inpHead = forms.CharField(label='Header on Input Sheet')
    outHead = forms.ChoiceField(label='Database Header', choices=HEADER_OPTIONS)

    def __init__(self, user, *args, **kwargs):
        super(HeaderForm, self).__init__(*args, **kwargs)
        self.user = user

class BrokerForm(forms.Form):
    inpBroker = forms.CharField(label='Broker on Input Sheet')
    outBroker = forms.CharField(label='Report Broker')

    def __init__(self, user, *args, **kwargs):
        super(BrokerForm, self).__init__(*args, **kwargs)
        self.user = user

class OutputForm(forms.Form):
    brokers = Transaction.objects.values("broker")
    BROKERS = ()
    for i in brokers:
        broker = (i['broker'], i['broker'])
        if broker not in BROKERS:
            BROKERS += (broker),

    brok = forms.ChoiceField(label='Broker', choices=BROKERS)
    start_date = forms.DateField(widget=forms.DateInput)
    end_date = forms.DateField(widget=forms.DateInput)

    def __init__(self, *args, **kwargs):
        super(OutputForm, self).__init__(*args, **kwargs)

class SummaryForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput)
    end_date = forms.DateField(widget=forms.DateInput)

    def __init__(self, *args, **kwargs):
        super(SummaryForm, self).__init__(*args, **kwargs)


class TradeMatchForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ()

    sales = Transaction.objects.filter(type='Sell').exclude(matching='Matched').exclude(shareamount=0)
    SALES = ()

    for i in sales:
        sale = (i.prim_key, str(i.symbol) + " " + str(i.shareamount) + " Shares Sold " + str(i.tradedate))
        if sale not in SALES:
            SALES += (sale),

    saleF = forms.ChoiceField(label='Sale Trade', choices=())
    all_purchases = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=(), required = False)
    matched_trades = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
