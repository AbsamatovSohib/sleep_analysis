from cart import models, serializer
from rest_framework import generics, views, response, status
from django.db.models import Sum, F, Subquery
from django.db.models.functions import Coalesce


class CartItemView(generics.ListAPIView):
    queryset = models.CartItems.objects.all().select_related("item")
    serializer_class = serializer.CartItemSerializer

    def get_queryset(self):
        total = self.queryset.filter(user=self.request.user).annotate(
            total=Sum(F('item__price') * F('quantity')))
        return total


class CartTotalPriceAPIView(generics.ListAPIView):
    queryset = models.CartItems.objects.all()
    serializer_class = serializer.Fornow

    def get_queryset(self):
        total = self.queryset.filter(user=self.request.user).annotate(
            total=Sum(F('item__price') * F('quantity'))).aggregate(
            total_sum=Sum("total"))

        return [total]



