from rest_framework import serializers
from sleep.models import Element, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title", )


class ElementSerializer(serializers.ModelSerializer):
    types = serializers.StringRelatedField(source="categories.title")

    class Meta:
        model = Element
        fields = ("title", "image", "price", "description", "types", "rating")
