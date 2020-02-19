from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from cartitem.models import CartItem
from api.serializers import CartItemSerializer

class CartItemList(APIView):
    def get(self, request):
        cartItems = CartItem.objects.all()
        data = CartItemSerializer(cartItems, many=True).data
        return Response(data)

class CartItemDetail(APIView):
    def get(self, request, pk):
        cartItems = get_object_or_404(CartItem, pk=pk)
        data = CartItemSerializer(cartItems).data
        return Response(data)
