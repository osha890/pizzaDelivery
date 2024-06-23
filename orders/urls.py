from django.urls import path
from .views import *

urlpatterns = [
    path('create-order/', order_view, name='create_order')
]
