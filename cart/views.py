from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Cart, CartItem
from .forms import DeleteFromCartForm


@login_required
def cart_view(request):
    if request.method == 'GET':
        cart = Cart.objects.filter(user=request.user).first()
        cart_items = CartItem.objects.filter(cart=cart)
        form = DeleteFromCartForm()
        context = {
            'cart_items': cart_items,
            'form': form,
            'title': 'Cart',
        }
        return render(request, 'cart/cart.html', context)
    elif request.method == 'POST':
        form = DeleteFromCartForm(request.POST)
        if form.is_valid():
            ci_id = form.cleaned_data['ci_id']
            ci = CartItem.objects.filter(id=ci_id, cart__user=request.user).first()
            if ci:
                ci.delete()
                return redirect('success')
    return redirect('cart')

