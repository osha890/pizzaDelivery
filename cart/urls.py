from django.urls import path
from .views import *

urlpatterns = [
    path('api/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('api/update_cart_item/', update_cart_item, name='update_cart_item'),
]