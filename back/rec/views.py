from urllib import request
import rec.utils.cron 
from rec.models import *
from rec.serializers import *
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ApartmentsList(generics.ListCreateAPIView):
    queryset = Apartments.objects.all()
    serializer_class  = ApartmentsSerializer

class ApartmentstDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartments.objects.all()
    serializer_class  = ApartmentsSerializer

class SearchApartmentsList(APIView):
    def get(self, request, format=None):
        queryset = Apartments.objects.all()
        serializer = ApartmentsSerializer(queryset, many=True)
        print(serializer)
        return Response(serializer.data)