from django.db import models


class ProductTotal(models.Manager):
    def total_sum(self):
        query = self.queryset
        return query.annotate(total_element_sum=self.quantity*self.element.price)

