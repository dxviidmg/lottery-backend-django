from rest_framework import viewsets
from .serializers import CardSerializer
from .models import Card
from django.db.models import F
from random import random

class CardViewSet(viewsets.ModelViewSet):
#    queryset = Card.objects.annotate(random_order=F('pk')*random()).order_by('random_order')
    queryset = Card.objects.all()
    serializer_class = CardSerializer