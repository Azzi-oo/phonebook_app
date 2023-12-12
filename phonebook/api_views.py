from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets


@csrf_exempt
def persone_list(request):
    if request.method == 'GET':
        persons = models.Persone.objects.all()
        serializers = serializers.PersoneSerializers(persons, many=True)
        return JsonResponse(serializers.data, safe=False)
    elif request.method == 'POST':
        persone = request.POST
        serializers = serializers.PersoneSerializers(data=persone)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)


class PersoneListAPIView(generics.ListAPIView):
    queryset = models.Persone.objects.all()
    serializer_class = serializers.PersoneSerializers


class PersonDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Persone.objects.all()
    serializer_class = serializers.PersoneSerializers


class PersoneUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Persone.objects.all()
    serializer_class = serializers.PersoneSerializers


class PersoneDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Persone.objects.all()
    serializer_class = serializers.PersoneSerializers


class PersoneModelViewSet(viewsets.ModelViewSet):
    queryset = models.Persone.objects.all()
    serializer_class = serializers.PersoneSerializers
