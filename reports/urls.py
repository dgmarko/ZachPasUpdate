from django.conf.urls import re_path, url
from django.urls import path
from .import views
from .views import OutputData, TradeMatchView, SummaryView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('datainput', views.input_data, name='input_data'),
    url(r'tradematch/$', login_required(TradeMatchView.as_view(success_url="tradematch")), name='trade_match'),
    url(r'output/$', login_required(OutputData.as_view(success_url="output")), name='output'),
    path('summary', login_required(SummaryView.as_view(success_url="summary")), name='summary_tab'),
    path(r'^ajax/load-purchases/$', views.load_purchases, name='load_buys'),
    path(r'^ajax/load-sales/$', views.load_sales, name='load_sales'),
    path(r'^ajax/load-brokers/$', views.load_brokers, name='load_brokers'),
    path('datainput/export_csv', views.export_csv, name='export_csv'),
]
