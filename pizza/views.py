from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Pizza
from .forms import AddToCartForm

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
            return redirect('catalog')
    else:
        form = AddToCartForm()

    return render(request, 'pizza/catalog.html', {'pizzas': pizzas, 'form': form})
