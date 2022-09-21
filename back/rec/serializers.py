from rest_framework import serializers
from rec.models import *


class ApartmentsSerializer(serializers.ModelSerializer):
    price_info = serializers.StringRelatedField(many=True)

    class Meta:
        model = Apartments
        fields = ['id', 'name', 'price_info']


class PriceInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PriceInfo
        fields = ['id', 'apart', 'date', 'price', 'per_price']
