from django.db import models


# Create your models here.

class Crypto(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=11)
    price = models.CharField(max_length=30)
    market_cap = models.CharField(max_length=30)
    circulating_supply = models.CharField(max_length=30)
    volume = models.CharField(max_length=30)
    change_1h = models.CharField(max_length=10)
    change_24h = models.CharField(max_length=10)
    change_7d = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']
