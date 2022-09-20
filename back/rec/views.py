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
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        queryset = Apartments.objects.all()

        # cron = Cron()
        # cron.make_csv()
        # cron.make_json()
        serializer = ApartmentsSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApartmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
