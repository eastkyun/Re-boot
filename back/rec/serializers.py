from rest_framework import serializers
from rec.models import Rec


class RecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rec
        fields = ['id', 'title', 'content']
