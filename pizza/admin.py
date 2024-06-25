from django.contrib import admin
from .models import *


# ---------PIZZA---------

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', ]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['category', 'size_name', 'price']
    list_editable = ['price', ]

    def size_name(self, obj):
        return obj.size.name
