from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Cart

##-------------- Cart Views --------------------------------------
class DetailCart(DetailView):
    model = Cart
    template_name='cart/detail_cart.html'

class ListCart(ListView):
    model = Cart
    context_object_name = 'carts'
    template_name='cart/list_carts.html'

class CreateCart(CreateView):
    model = Cart
    template_name = 'cart/create_cart.html'

class Updatecart(UpdateView):
    model = Cart
    template_name = 'cart/update_cart.html'

class DeleteCart(DeleteView):
    model = Cart
    template_name = 'cart/delete_cart.html'


