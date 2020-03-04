from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import CartItem
from .forms import CartItemForm
# from cart.models import Cart


class DetailCartItem(DetailView):
    model = CartItem
    template_name='cartitem/detail_cartitem.html'

class ListCartItem(ListView):
    model = CartItem
    def get(self, request):
        items = self.get_queryset().all()
        return render(request, 'cartitems.html', {'items': items})

class CreateNewCartItem(CreateView):
    def get(self, request):
        content = {'form': CartItemForm()}
        return render(request, 'cartitem/create_new_cartitem.html', content)

    def post(self, request):
        form = CartItemForm(request.POST)
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.user = 'test'
            # instance.save()
            form.save()
            return HttpResponseRedirect(reverse_lazy('list-cartitem'))
        return render(request, 'cartitem/create_new_cartitem.html', {'form': form})

class UpdateCartItem(UpdateView):
    model = CartItem
    template_name = 'cartitem/update_cartitem.html'

class DeleteCartItem(DeleteView):
    model = CartItem
    template_name = 'cartitem/delete_cartitem.html'

