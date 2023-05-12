from rest_framework import serializers
from .models import Crypto, PercentageChange


class PercentageChangeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = PercentageChange
        fields = ['change_1h','change_24h', 'change_7d' ]

class CryptoSerializer(serializers.ModelSerializer):
    percent_change = PercentageChangeSerialzer()
    class Meta:
        model = Crypto
        fields = ['rank', 'name', 'symbol', 'price', 'market_cap', 'circulating_supply', 'volume', 'percent_change']

