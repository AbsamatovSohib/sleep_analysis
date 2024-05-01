from cart.models import CartItems
from sleep.serializer import ElementSerializer
from rest_framework import serializers


class CartItemSerializer(serializers.ModelSerializer):
    item = ElementSerializer()
    total = serializers.IntegerField()

    class Meta:
        model = CartItems
        fields = ("item", "quantity", "total")



class Fornow(serializers.ModelSerializer):

    total_sum = serializers.StringRelatedField()
    class Meta:
        model  = CartItems
        fields = (
            'total_sum',
        )







