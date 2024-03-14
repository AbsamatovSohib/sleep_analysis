from django.db import models
from sleep.models import Element


class Cart(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="shop_cart")
    item = models.ForeignKey(Element, on_delete=models.CASCADE, related_name="element")

    quantity = models.PositiveIntegerField(default=0)
