from django.shortcuts import render
from intro import models, serializer
from rest_framework import generics


class IntroListView(generics.ListAPIView):
    queryset = models.Intro.objects.all()
    serializer_class = serializer.IntroSerializer


class NotificationListView(generics.ListAPIView):
    queryset = models.Notifications.objects.all()
    serializer_class = serializer.NotificationSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
