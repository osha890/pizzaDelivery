from django.urls import path
from .views import *

urlpatterns = [
    path('create-order/', create_order_view, name='create_order'),
    path('', orders_view, name='orders')
]
