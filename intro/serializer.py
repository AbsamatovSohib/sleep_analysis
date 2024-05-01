from rest_framework import serializers
from intro import models


class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Intro
        fields = ("title", "image")


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notifications
        fields = ("title", "description")
