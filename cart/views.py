from cart import models, serializer
from rest_framework import generics
from django.db.models import Sum

class CartItemsListView(generics.ListAPIView):
    queryset = (models.Cart.objects.all()
                .prefetch_related(
        "shop_cart",
        "shop_cart__item",
    ))


    serializer_class = serializer.CartSerializer

    def get_queryset(self):
        query = self.queryset
        query = query.annotate(total=Sum(self.queryset.aggregate()))


