from django.shortcuts import render, redirect

from cart.models import Cart
from django.utils import timezone

from orders.models import Order, OrderItem


def order_view(request):
    if request.method == 'POST':
        user = request.user
        cart = Cart.objects.filter(user=user).first()
        if cart:
            cis = cart.cartitem_set.all()
            if cis:
                order = Order.objects.create(user=user, created_at=timezone.now(), order_price=0)
                order_price = 0
                for ci in cis:
                    item_price = ci.get_total_price()
                    OrderItem.objects.create(order=order,
                                             pizza=ci.pizza,
                                             size=ci.size,
                                             quantity=ci.quantity,
                                             item_price=item_price)
                    ci.delete()
                    order_price += item_price
                order.order_price = order_price
                order.save()
                return redirect('success')
    return redirect('cart')
