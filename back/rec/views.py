# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rec.models import *
from rec.serializers import *

class ApartmentsList(APIView):
    """
    List all apartments, or create a new apartments.
    """
    def get(self, request, format=None):
        apartments = Apartments.objects.all()
        serializer = ApartmentsSerializer(apartments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApartmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApartmentstDetail(APIView):
    """
    Retrieve, update or delete a apartments instance.
    """
    def get_object(self, pk):
        try:
            return Apartments.objects.get(pk=pk)
        except Apartments.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        apartments = self.get_object(pk)
        serializer = ApartmentsSerializer(apartments)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        apartments = self.get_object(pk)
        serializer = ApartmentsSerializer(apartments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        apartments = self.get_object(pk)
        apartments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)