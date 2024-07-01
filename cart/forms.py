from django import forms
from pizza.models import Size
from cart.models import CartItem


# def get_sizes():
#     sizes = []
#     for s in Size.objects.all():
#         sizes.append((s.size, s.name))
#     return sizes


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['size', 'quantity']

    size = forms.ModelChoiceField(queryset=Size.objects.all())
    quantity = forms.IntegerField(min_value=1, initial=1)


class DeleteFromCartForm(forms.Form):
    ci_id = forms.IntegerField(widget=forms.HiddenInput())
