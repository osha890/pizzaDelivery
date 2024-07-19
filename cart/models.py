from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pizza.models import Pizza, Size, Price


# ---------CART---------

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}'

    def get_total_price(self):
        total_price = 0
        items = self.cartitem_set.select_related('pizza', 'size').all()
        for item in items:
            total_price += item.get_total_price()
        return total_price


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    first_added_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return Price.objects.get(category=self.pizza.category, size=self.size).price * self.quantity

    def save(self, *args, **kwargs):  # Override
        self.last_added_at = timezone.now()  # Обновляем поле last_added_at перед сохранением
        super().save(*args, **kwargs)  # Вызываем метод save родительского класса

    def __str__(self):
        return f'Cart {self.cart.pk}: {self.pizza} {self.size}'
