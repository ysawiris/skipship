from django import forms
from cartitem.models import CartItem

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['user', 'product', 'quantity', 'cart']