from urllib import request
from rec.utils.cron import Cron
from rec.models import *
from rec.serializers import *
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ApartmentsList(generics.ListCreateAPIView):
    queryset = Apartments.objects.all()
    serializer_class = ApartmentsSerializer


class ApartmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartments.objects.all()
    serializer_class = ApartmentsSerializer


class PriceInfoList(generics.ListCreateAPIView):
    queryset = PriceInfo.objects.all()
    serializer_class = PriceInfoSerializer


class PriceInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceInfo.objects.all()
    serializer_class = PriceInfoSerializer


class SearchApartmentsList(APIView):
    def get(self, request, format=None):
        apartments = Apartments.objects.all()
        apartments_serializer = ApartmentsSerializer(apartments, many=True)

        crawling_list = Cron.crawling_rec_api(apartments_serializer.data)
        for info in crawling_list:
            apart_id = Apartments.objects.get(pk=info['apart'])
            price_info = PriceInfo(apart=apart_id, price=info['price'], per_price=info['per_price'])
            price_info.save()
        return Response(apartments_serializer.data)
