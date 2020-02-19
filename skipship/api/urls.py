from django.urls import path

from api.views import CartItemDetail, CartItemList

urlpatterns = [
    path('', CartItemList.as_view(), name='cartItem_list'),
    path('<int:pk>', CartItemDetail.as_view(), name='cartItem_detail')
]