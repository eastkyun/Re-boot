import os
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rec.models import Rec
from rec.serializers import RecSerializer
from rec.utils.price import Price


@csrf_exempt
def rec_list(request):
    """
    List all code Recs, or create a new Rec.
    """
    if request.method == 'GET':
        rec_data = Price.getData()
        return JsonResponse(rec_data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = RecSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def rec_list_shorts(request, pk):
    """
    List all code Recs, or create a new Rec.
    """
    if request.method == 'GET':
        rec_data = Price.getData(pk)
        return JsonResponse(rec_data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = RecSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def rec_detail(request, pk):
    """
    Retrieve, update or delete a code Rec.
    """
    try:
        rec = Rec.objects.get(pk=pk)
    except Rec.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RecSerializer(rec)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RecSerializer(rec, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        rec.delete()
        return HttpResponse(status=204)
