from django.contrib import admin
from .models import *


# ---------CART---------

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'pizza', 'size', 'quantity', 'first_added_at', 'last_edited_at']
    list_display_links = ['pizza',]