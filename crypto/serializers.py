from rest_framework import serializers
from .models import Crypto


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = '__all__'

    def create(self, validated_data):
        return Crypto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rank = validated_data.get('rank', instance.rank)
        instance.name = validated_data.get('name', instance.name)
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.price = validated_data.get('price', instance.price)
        instance.market_cap = validated_data.get('market_cap', instance.market_cap)
        instance.circulating_supply = validated_data.get('circulating_supply', instance.circulating_supply)
        instance.volume = validated_data.get('volume', instance.volume)
        instance.change_1h = validated_data.get('change_1h', instance.change_1h)
        instance.change_24h = validated_data.get('change_24h', instance.change_24h)
        instance.change_7d = validated_data.get('change_7d', instance.change_7d)
        instance.save()
        return instance
