from django.urls import path
from . import views


urlpatterns = [
    path('', views.stock_list, name='index'),
    path('chart/', views.stock_chart, name='chart'),
]