import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Cart, CartItem


@login_required
def cart_view(request):
    if request.method == 'GET':
        cart = Cart.objects.filter(user=request.user).first()
        cart_items = CartItem.objects.filter(cart=cart)
        context = {
            'cart_items': cart_items,
            'title': 'Cart',
        }
        return render(request, 'cart/cart.html', context)
    # elif request.method == 'POST':
    #     ci_id = int(request.POST.get('ci_id'))
    #     ci = CartItem.objects.filter(id=ci_id, cart__user=request.user).first()
    #     if ci:
    #         ci.delete()
    #         return redirect('success')
    return redirect('cart')


def update_quantity(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')
            action = data.get('action')

            print(f"Received item_id: {item_id}, action: {action}")  # Добавим отладочный вывод

            if item_id is None or action is None:
                return JsonResponse({'error': 'Invalid data'}, status=400)

            item = CartItem.objects.get(id=item_id)

            if action == 'decrease' and item.quantity == 1:
                item.delete()
                return JsonResponse({'error': 'item deleted'})  # Отправим специальный ответ
            elif action == 'decrease':
                item.quantity -= 1
                item.save()
            elif action == 'increase':
                item.quantity += 1
                item.save()

            return JsonResponse({'quantity': item.quantity})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
