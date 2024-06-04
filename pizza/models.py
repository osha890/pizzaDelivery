from django.contrib.auth.models import User
from django.db import models


# ---------PIZZA---------

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.size} cm'


class Price(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category', 'size'], name='unique_category_size')
        ]

    def __str__(self):
        return f'{self.size} {self.category}'


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


# ---------CART---------

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return Price.objects.get(category=self.pizza.category, size=self.size) * self.quantity

    def __str__(self):
        return f'Cart {self.cart.pk}: {self.pizza} {self.size}'
