from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cart.models import Cart
from cart.forms import CartForm

##-------------- Cart Views --------------------------------------
class Homepage(ListView):
    model = Cart
    template_name='cart/homepage.html'

class DetailCart(DetailView):
    model = Cart
    template_name='cart/detail_cart.html'

class ListCart(ListView):
    model = Cart
    context_object_name = 'carts'
    template_name='cart/list_carts.html'

class OrderCart(ListView):
    model = Cart
    template_name = 'cart/order_cart.html'

class Updatecart(UpdateView):
    model = Cart
    template_name = 'cart/update_cart.html'

class DeleteCart(DeleteView):
    model = Cart
    template_name = 'cart/delete_cart.html'

class CreateNewCart(CreateView):
    def get(self, request):
        content = {'form': CartForm()}
        return render(request, 'cart/create_new_cart.html', content)

    def post(self, request):
        form = CartForm(request.POST)
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.user = 'test'
            # instance.save()
            form.save()
            return HttpResponseRedirect(reverse_lazy('list-carts'))
        return render(request, 'cart/create_new_cart.html', {'form': form})