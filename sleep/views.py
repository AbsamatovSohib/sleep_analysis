from sleep import models, serializer
from rest_framework import generics


class ElementListView(generics.ListAPIView):
    queryset = models.Element.objects.all()
    serializer_class = serializer.ElementSerializer
