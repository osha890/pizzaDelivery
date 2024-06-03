from django.contrib import admin
from .models import *


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
