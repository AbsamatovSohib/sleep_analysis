from django.db import models
from sleep.choices import MY_SLEEP_CHOICES, RatingChoices
# from multiselectfield import MultiSelectField
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=127)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Element(models.Model):
    title = models.CharField(max_length=257)
    image = models.ImageField(upload_to="images/")
    price = models.PositiveIntegerField()
    description = models.TextField()

    # types = MultiSelectField(choices=MY_SLEEP_CHOICES, max_choices=7, max_length=100)
    types = models.ManyToManyField(Category, related_name="categories")
    rating = models.CharField(choices=RatingChoices.choices, max_length=10)

    def __str__(self):
        return self.title
