from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Pizza
from .forms import AddToCartForm

from cart.models import Cart, CartItem

@login_required
def catalog_view(request):
    pizzas = Pizza.objects.all()
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            pizza_id = form.cleaned_data['pizza_id']
            quantity = form.cleaned_data['quantity']
            size = form.cleaned_data['size']
            # Здесь вы можете добавить код для добавления пиццы в корзину пользователя

            cart, created = Cart.objects.get_or_create(user=request.user, defaults={'created_at': timezone.now()})

            cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza_id=pizza_id, size=size, defaults={
                'quantity': quantity,
                'first_added_at': timezone.now(),
                'last_edited_at': timezone.now()
            })

            if not created:
                # Если элемент уже существует, увеличиваем количество
                cart_item.quantity += quantity
                cart_item.last_edited_at = timezone.now()
                cart_item.save()

            return redirect('catalog')
    else:
        form = AddToCartForm()

    return render(request, 'pizza/catalog.html', {'pizzas': pizzas, 'form': form})
