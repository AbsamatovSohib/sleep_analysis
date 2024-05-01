from rest_framework import serializers
from users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "email",
            "name",
            "image",
            "phone_number",
            "height",
            "weight",
            "blood_gr",
            "age",
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "name",
            "image",
            "phone_number",
            "height",
            "weight",
            "blood_gr",
            "age",
        )
