from cart.models import Cart, CartItems
from sleep.serializer import ElementSerializer
from rest_framework import serializers


class CartItemSerializer(serializers.ModelSerializer):
    item = ElementSerializer()

    class Meta:
        model = CartItems
        fields = ("item", "quantity", )


class CartSerializer(serializers.ModelSerializer):
    shop_cart = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ("title", "shop_cart")
