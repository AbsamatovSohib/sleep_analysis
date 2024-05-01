from django.db import models
from sleep.models import Element
from django.contrib.auth import get_user_model
from utils.common import BaseModel

User = get_user_model()


class CartItems(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    item = models.ForeignKey(Element, on_delete=models.CASCADE, related_name="element")

    quantity = models.PositiveIntegerField(default=0)

    # total_sum = models.IntegerField(null=True, blank=True)
    #
    # def total_sum(self):
    #     return self.quantity*self.item.price


