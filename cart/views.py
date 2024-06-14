from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Cart, CartItem


@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/cart.html', {'cart_items': cart_items})
