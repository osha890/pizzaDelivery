from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from pizza.models import Pizza, Size, Category
from cart.forms import AddToCartForm

from cart.models import Cart, CartItem


def pizza_list_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            pizza_id = int(request.POST.get('pizza_id'))
            size_id = int(request.POST.get('size'))
            # quantity = int(request.POST.get('quantity'))
            cart, created = Cart.objects.get_or_create(user=request.user, defaults={'created_at': timezone.now()})

            cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza_id=pizza_id, size=Size.objects.get(id=size_id), defaults={
                'quantity': 1,
                'first_added_at': timezone.now(),
                'last_edited_at': timezone.now()
            })

            if not created:
                cart_item.quantity += 1
                cart_item.last_edited_at = timezone.now()
                cart_item.save()

        # return redirect('success')
            return JsonResponse({'status': 'success', 'message': 'Item added to cart'})
        else:
            # return redirect('login')
            return JsonResponse({'status': 'error', 'message': 'User not authenticated'})
    elif request.method == 'GET':
        cats = Category.objects.all()
        form = AddToCartForm()
        context = {
            'title': 'Home page',
            'cats': cats,
            'form': form,
        }
        return render(request, 'pizza_list.html', context)


def success_view(request):
    return render(request, 'success.html', {'title': 'Success'})
