from rest_framework.serializers import ModelSerializer

from cartitem.models import CartItem

class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
