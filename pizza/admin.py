from django.contrib import admin
from .models import *


# ---------PIZZA---------

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['category', 'size', 'price']
    list_editable = ['price', ]


# ---------CART---------

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'pizza', 'size', 'quantity', 'added_at']
