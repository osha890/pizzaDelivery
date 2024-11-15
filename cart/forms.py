from django import forms
from pizza.models import Size


def get_sizes():
    sizes = []
    try:
        for s in Size.objects.all():
            sizes.append((s.id, s.name))
    except Exception as e:
        print(e)
    return sizes


class AddToCartForm(forms.Form):
    size = forms.ChoiceField(
        choices=get_sizes(),
        widget=forms.RadioSelect
    )
    # quantity = forms.IntegerField(min_value=1, initial=1)
    pizza_id = forms.IntegerField(widget=forms.HiddenInput())


# class DeleteFromCartForm(forms.Form):
#     ci_id = forms.IntegerField(widget=forms.HiddenInput())
