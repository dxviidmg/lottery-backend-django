from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/cards/')

    def __str__(self) -> str:
        return self.name
