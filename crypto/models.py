from django.db import models


# Create your models here.
class PercentageChange(models.Model):
    change_1h = models.CharField(max_length=10)
    change_24h = models.CharField(max_length=10)
    change_7d = models.CharField(max_length=10)


class Crypto(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=11)
    price = models.CharField(max_length=30)
    market_cap = models.CharField(max_length=30)
    circulating_supply = models.CharField(max_length=30)
    volume = models.CharField(max_length=30)
    percent_change = models.ForeignKey(PercentageChange, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']