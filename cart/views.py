from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pizza.models import Pizza
from cart.models import Cart, CartItem

from .serializers import CartItemSerializer


@api_view(['POST'])
def add_to_cart(request):
    user = request.user
    pizza_id = request.data.get('pizza_id')
    quantity = request.data.get('quantity', 1)

    if not pizza_id:
        return Response({'error': 'Pizza ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    pizza = Pizza.objects.get(id=pizza_id)
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, pizza=pizza)

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()

    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def update_cart_item(request):
    item_id = request.data.get('item_id')
    quantity = request.data.get('quantity')

    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.quantity = quantity
        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
