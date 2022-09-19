from rest_framework import serializers
from rec.models import *


class ApartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartments
        fields = ['id', 'name']


class PriceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceInfo
        fields = ['id', 'apart', 'date', 'price']
