from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import Http404

from .models import CartItem
from .forms import CartItemForm


class DetailCartItem(DetailView):
    model = CartItem

    def get(self, request, pk):
        """ Returns a specific wiki page by slug. """
        pass
        cartitem = self.get_queryset().get(pk=pk)
        return render(request, 'cartitem/detail_cartitems.html', {
          'cartitem': cartitem
        })


class ListCartItem(ListView):
    model = CartItem
    def get(self, request):
        items = self.get_queryset().all()
        return render(request, 'cartitem/cartitems.html', {'items': items})

class CreateNewCartItem(CreateView):
    model = CartItem

    def get(self, request):

        content = {'form': CartItemForm()}
        return render(request, 'cartitem/create_new_cartitem.html', content)


    def post(self, request):
        form = CartItemForm(request.POST)
        if form.is_valid():
            cartItem = form.save(commit=False)
            cartItem.user = request.user
            cartItem.save()
            return HttpResponseRedirect(reverse('cartitem:detail-cartitem', args=[cartItem.id]))


        content = {'form': CartItemForm()}
        return render(request, 'cartitem/create_new_cartitem.html', content)


class UpdateCartItem(UpdateView):
    model = CartItem
    form_class = CartItemForm
    template_name = 'cartitem/update_cartitem.html'
    queryset = CartItem.objects.all()



def deleteCartItem(request, pk):
    apple = get_object_or_404(CartItem, pk=pk)
    apple.delete()
    return HttpResponseRedirect(reverse('cartitem:list-cartitem'))