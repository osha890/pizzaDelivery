from django.contrib.auth.models import User
from django.db import models

from pizza.models import Pizza, Size


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.pk}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    item_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.order}: {self.pizza} {self.size}'
