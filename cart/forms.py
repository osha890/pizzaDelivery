from django import forms
from pizza.models import Size


class AddToCartForm(forms.Form):
    size = forms.ModelChoiceField(queryset=Size.objects.all(), empty_label=None)
    quantity = forms.IntegerField(min_value=1, initial=1)
    pizza_id = forms.IntegerField(widget=forms.HiddenInput())
