from django.shortcuts import render, redirect
from django.utils import timezone
from pizza.models import Pizza
from cart.forms import AddToCartForm

from cart.models import Cart, CartItem


def pizza_list_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AddToCartForm(request.POST)
            if form.is_valid():
                pizza_id = form.cleaned_data['pizza_id']
                size = form.cleaned_data['size']
                quantity = form.cleaned_data['quantity']

                cart, created = Cart.objects.get_or_create(user=request.user, defaults={'created_at': timezone.now()})

                cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza_id=pizza_id, size=size, defaults={
                    'quantity': quantity,
                    'first_added_at': timezone.now(),
                    'last_edited_at': timezone.now()
                })

                if not created:
                    cart_item.quantity += quantity
                    cart_item.last_edited_at = timezone.now()
                    cart_item.save()

            return redirect('success')
        else:
            return redirect('login')
    elif request.method == 'GET':
        pizzas = Pizza.objects.all()
        form = AddToCartForm()
        context = {
            'title': 'Home page',
            'pizzas': pizzas,
            'form': form,
        }
        return render(request, 'pizza_list.html', context)


def success_view(request):
    return render(request, 'success.html', {'title': 'Success'})
