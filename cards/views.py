from rest_framework import viewsets
from .serializers import CardSerializer
from .models import Card
from django.db.models import F
from random import random

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.order_by('?')
    serializer_class = CardSerializer